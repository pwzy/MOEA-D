#ifndef __MOEAD_H_
#define __MOEAD_H_

#include "global.h"
#include "common.h"
#include "individual.h"
#include "scalarfunc.h"
#include "recombination.h"

class TMOEAD    
{
public:

	TMOEAD();
	virtual ~TMOEAD();

	void init_uniformweight(int sd);    // initialize the weights for subproblems  对每个子问题初始化权重
	void init_neighbourhood();          // calculate the neighbourhood of each subproblem 计算每个问题的领域
	void init_population();             // initialize the population  初始化种群


	void update_reference(TIndividual &ind);           // update the approximation of ideal point
	void update_problem(TIndividual &child, int id);   // compare and update the neighboring solutions
	void evolution();                                  // mating restriction, recombination, mutation, update
	void run(int sd, int nc, int mg, int rn);          // execute MOEAD
	void save_front(char savefilename[1024]);          // save the pareto front into files

    vector <TSOP>  population;  // current population      	   
	TIndividual *indivpoint;    // reference point
	int  niche;                 // neighborhood size  领域大小
	int  pops;                  // population   size 种群大小

	void operator=(const TMOEAD &emo);
};

TMOEAD::TMOEAD()
{

    // 参考目标向量：即切比雪夫聚合函数中的z*点，，将其初始化
	idealpoint = new double[numObjectives];
    // 参考点（每个目标函数就有有一个参考点，共有numObjectives个参考点）
	indivpoint = new TIndividual[numObjectives];    
	// initialize ideal point	随机初始化参考点并就计算参考点的值
    for(int n=0; n<numObjectives; n++) 
	{
		idealpoint[n] = 1.0e+30;  
		indivpoint[n].rnd_init();
		indivpoint[n].obj_eval();
	}
}

TMOEAD::~TMOEAD()
{
	delete [] idealpoint;    
	delete [] indivpoint;
}


void TMOEAD::init_population()  // 初始化种群
{
    for(int i=0; i<pops; i++)
	{
		population[i].indiv.rnd_init();  // 种群中每个个体进行随机初始化
		population[i].indiv.obj_eval();  // 计算种群中每个个体的目标函数值
		update_reference(population[i].indiv);  // 更新参考点
	}
}

// 对子问题初始化权重向量
// initialize a set of evely-distributed weight vectors
void TMOEAD::init_uniformweight(int sd) // 生成权重向量
{
	// sd: integer number for generating weight vectors 生成权重向量的整数（权重向量的个数等于种群规模个数）
    for(int i=0; i<=sd; i++)
	{
		if(numObjectives==2)
		{
            TSOP sop;		   
			sop.array.push_back(i);
			sop.array.push_back(sd-i);
		    for(int j=0; j<sop.array.size(); j++)
				sop.namda.push_back(1.0*sop.array[j]/sd);
			population.push_back(sop); 
		}
		else
		{
			for(int j=0;j<=sd;j++)
			{
				if(i+j<=sd)
				{
				    TSOP sop;		   
					sop.array.push_back(i);
					sop.array.push_back(j);
					sop.array.push_back(sd-i-j);
		            for(int k=0; k<sop.array.size(); k++)
						sop.namda.push_back(1.0*sop.array[k]/sd);
					population.push_back(sop); 
				}
			}
		}
	}
	pops = population.size();
}
// 基于权重向量初始化子问题的领域
// initialize the neighborhood of subproblems based on the distances of weight vectors
void TMOEAD::init_neighbourhood()
{
    double *x   = new double[pops];
	int    *idx = new int[pops];
	for(int i=0; i<pops; i++)
	{	
		for(int j=0; j<pops; j++)   // 计算权重的欧式距离
		{
		    x[j]    = distanceVector(population[i].namda,population[j].namda);
			idx[j]  = j;			
		}
		minfastsort(x,idx,pops,niche);   
		for(int k=0; k<niche; k++)   
			population[i].table.push_back(idx[k]);  //将索引值存储在个体的领域表中

	}
    delete [] x; // 进行内存的释放
	delete [] idx;
}

// 传入的参数为交叉变异后的个体和当前正在操作的向量  indiv：交叉变异后的个体，id：当前正在操作的向量
// update the best solutions of neighboring subproblems
void TMOEAD::update_problem(TIndividual &indiv, int id)
{
    for(int i=0; i<niche; i++)  // 对正在操作中的向量的每一个领域中的向量进行遍历
	{
		// 此处即采取聚合函数的方法进行正在操作的个体与交叉变异后的个体的比较，从而进行个体的更新
		int k  = population[id].table[i];  // k代表正在操作的向量的领域中的每一个向量（随着迭代分别代表 第1，2。。。niche个向量）
		double f1, f2;  // 定义目标函数值
		f1 = scalar_func(population[k].indiv.y_obj, population[k].namda, indivpoint);
		f2 = scalar_func(indiv.y_obj, population[k].namda, indivpoint);
		if(f2<f1) population[k].indiv = indiv;  // 见MOEA/D的第2.4步
	}
}


// update the reference point  更新参考点
void TMOEAD::update_reference(TIndividual &ind)
{
	for(int n=0; n<numObjectives; n++)    
	{
        // 若rnd对象的目标函数向量支配idealpoint向量，则将idealpoint向量更新为rnd对象的目标函数向量，并将参考点设置为此点
		// 即如果个体支配参考点，则进行参考点的更新
		if(ind.y_obj[n]<idealpoint[n])
		{
			idealpoint[n]  = ind.y_obj[n];
			indivpoint[n]  = ind;
		}		
	}
}


// recombination, mutation, update in MOEA/D  //进行一次进化操作，其中包含基因重组，突变操与更新操作
void TMOEAD::evolution()
{
    for(int i=0; i<population.size(); i++)  // 对种群中的每个个体进行操作
	{
		int   n  =  i;    // n代表当前正在进行操作的个体
		int   s  = population[n].table.size();    // s代表此个体领域的大小
		int   r1 = int(s*rnd_uni(&rnd_uni_init));  // r1代表生成0-s中的一个整数
		int   r2 = int(s*rnd_uni(&rnd_uni_init));  // r2同上
		int   p1 = population[n].table[r1];    // p1代表在领域中随机选中的一个个体
		int   p2 = population[n].table[r2];    // p2代表在领域中随机选中的另一个个体
		TIndividual child, child2;   // 定义两个子个体为child1与child2
		realbinarycrossover(population[p1].indiv,population[p2].indiv,child, child2);    //进行交叉操作
		realmutation(child, 1.0/numVariables);  // //进行突变操作
		child.obj_eval();  // 计算新生成的子代的目标函数值
		update_reference(child);  // 更新参考点
		update_problem(child, n);  // 传入的参数为交叉变异后的个体和当前正在操作的向量
	}
}



void TMOEAD::run(int sd, int nc, int mg, int rn)
{
    // sd: integer number for generating weight vectors  sd：生成权重向量的整数
	// nc: size of neighborhood   nc：领域的大小
	// mg: maximal number of generations   mg： 最大的迭代次数
	// rn： 代表的是运行的次数
	niche = nc;	
	init_uniformweight(sd);
    init_neighbourhood();
	init_population();	
	for(int gen=2; gen<=mg; gen++)   evolution();      // 进行进化
	char savefilename[1024];
	// sprintf指的是字符串格式化命令，函数声明为 int sprintf(char *string, char *format [,argument,...]);，
	// 主要功能是把格式化的数据写入某个字符串中，即发送格式化输出到 string 所指向的字符串
	// sprintf(savefilename,"ParetoFront/DMOEA_%s_R%d.txt",strTestInstance,rn);
    sprintf(savefilename,"ParetoFront/DMOEA_%s_R%d.dat",strTestInstance,rn);
	save_front(savefilename);
	population.clear();
}


void TMOEAD::save_front(char saveFilename[1024])
{
	// 将fout对象与要输出的文件进行关联
    std::fstream fout;
	// 打开等待输入的文件，等待字符流的输入
	fout.open(saveFilename,std::ios::out);
	for(int n=0; n<population.size(); n++)  // 对种群中的每一个个体进行遍历
	{
		for(int k=0;k<numObjectives;k++)
			fout<<population[n].indiv.y_obj[k]<<"  ";  // 将个体的信息格式化输出到文件中
		fout<<"\n";
	}
	fout.close(); // 关闭打开的文件
}


void TMOEAD::operator=(const TMOEAD &emo)
{
    pops        = emo.pops;
	population  = emo.population;
	indivpoint  = emo.indivpoint;
	niche       = emo.niche;
} 


#endif