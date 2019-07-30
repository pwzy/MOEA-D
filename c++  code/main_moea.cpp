/*==========================================================================
//  Implementation of Multiobjective Evolutionary Algorithm Based on 
//  Decomposition (MOEA/D) For Continuous Multiobjective Optimization Problems (2006)
//
//  See the details of MOEA/D in the following paper
//  Q. Zhang and H. Li, MOEA/D: A Multi-objective Evolutionary Algorithm Based on Decomposition, 
//  IEEE Trans. on Evolutionary Computation, in press, 2007
//
//  The source code of MOEA/D was implemented by Hui Li and Qingfu Zhang  
//
//  If you have any questions about the codes, please contact 
//  Qingfu Zhang at qzhang@essex.ac.uk  or Hui Li at hzl@cs.nott.ac.uk
===========================================================================*/


#include "global.h"
#include "dmoea.h"

int main(void)
{

	// set the type of decomposition method
	// "_TCH1": Tchebycheff, "_TCH2": normalized Tchebycheff, "_PBI": Penalty-based BI
	// 采用切比雪夫聚合函数
    strcpy(strFunctionType,"_TCH1");  
    // 代码总运行次数
	int  total_run       = 1;         // totoal number of runs  总的运行次数
	int  max_gen         = 250;       // maximal number of generations  迭代的最大代数
	int  niche           = 20;        // neighborhood size  定义的领域的大小

	char const *instances[]  = {"ZDT1","ZDT2","ZDT3","ZDT4","ZDT6","DTLZ1","DTLZ2"}; // names of test instances  定义测试函数的名称
	int  nvars[]       = {30, 30, 30, 10, 10, 10, 10};                         // number of variables 定义每个测试实例变量的维度
	int  nobjs[]       = {2, 2, 2, 2, 2, 3, 3};                                // number of objectives 定义每个测试实例目标维度

	for(int n=0; n<7; n++)   // 分别对7个实例进行测试（迭代7次）
	{
		// strTestInstance 原型为：char strTestInstance[256];，用来存储每个实例的名称
		strcpy(strTestInstance,instances[n]);
		// numVariables存储变量维数
		numVariables  = nvars[n];
		// numObjectives存储目标维数
		numObjectives = nobjs[n];
		
		for(int run=1; run<=total_run; run++)
		{
			// 定义随机种子数 此数可任意设定
			// int seed = 237;
			// 随机设置一个种子
			seed = (seed + 111)%1235;	
			//rnd_uni_init： 64位的有符号整性，这个数是为了搭配randon.h中的rnd_uni函数，从而生成0-1之间的随机数
			// 由种子产生一个随机数
			rnd_uni_init = -(long)seed;	
			TMOEAD  MOEAD;      
			
			if(numObjectives==3)  MOEAD.run(23, niche, max_gen, run);  //23 -3  popsize 300

			if(numObjectives==2)  MOEAD.run(99, niche, max_gen, run);  //99 -2  popsize 100
		}		
	}
    return 0;
}