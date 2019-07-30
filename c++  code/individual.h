#ifndef __TINDIVIDUAL_H_
#define __TINDIVIDUAL_H_

//#include "global.h"
#include "objective.h"

class TIndividual{
public:
	TIndividual();
	virtual ~TIndividual();

	vector <double> x_var;  // 动态数组，用于存放自变量 x_var
	vector <double> y_obj;  // 动态数组，用于存放目标变量y_obj

	void   rnd_init(); // 随机初始化
	void   obj_eval(); // 计算目标函数

    bool   operator<(const TIndividual &ind2); // 对"<"号重载，重新赋予意义，使"<"能在个体之间比较
    bool   operator==(const TIndividual &ind2); // 对"=="号重载，重新赋予意义，使"=="能在个体之间比较
    void   operator=(const TIndividual &ind2); // 对"="号重载，重新赋予意义，使"="能在个体之间比较

	void show_objective();
	void show_variable();

	int    rank;

};

TIndividual::TIndividual()  // 构造函数
{
	for(int i=0; i<numVariables; i++)
		// 该函数将一个新的元素加到vector的最后面，位置为当前最后一个元素的下一个元素，新的元素的值是val的拷贝（或者是移动拷贝）
		x_var.push_back(0.0); // 自变量维度全部清零
	for(int n=0; n<numObjectives; n++)
        y_obj.push_back(0.0); // 实现目标变每个维度清零
	rank = 0;  // 初始化分类登记为：0
}

TIndividual::~TIndividual()  // 析构函数
{

}

void TIndividual::rnd_init()   //实现个体的随机初始化（每个维度为0-1之间的随机值）
{
    for(int n=0;n<numVariables;n++)
        x_var[n] = lowBound + rnd_uni(&rnd_uni_init)*(uppBound - lowBound);    

}

void TIndividual::obj_eval()  // 此函数用来计算目标给函数的值
{
    objectives(x_var,y_obj);
}


void TIndividual::show_objective()  // 显示目标变量的值
{
    for(int n=0; n<numObjectives; n++)
		printf("%f ",y_obj[n]);
	printf("\n");
}

void TIndividual::show_variable() // 显示个体的值
{
    for(int n=0; n<numVariables; n++)
		printf("%f ",x_var[n]);
	printf("\n");
}

void TIndividual::operator=(const TIndividual &ind2) // 实现"="运算符重载,实现个体属性的赋值
{
    x_var = ind2.x_var;
	y_obj = ind2.y_obj;
	rank  = ind2.rank;
}

bool TIndividual::operator<(const TIndividual &ind2) // 实现"<"运算符重载，实现个体支配性的比较
{
	bool dominated = true;
    for(int n=0; n<numObjectives; n++)
	{
		if(ind2.y_obj[n]<y_obj[n]) return false;
	}
	if(ind2.y_obj==y_obj) return false;
	return dominated;
}


bool TIndividual::operator==(const TIndividual &ind2) // 实现"=="运算符重载，实现每个个体的目标函数值的比较
{
	if(ind2.y_obj==y_obj) return true;
	else return false;
}



class TSOP 
{
public:
	TSOP();
	virtual ~TSOP();

	void show();

	TIndividual     indiv;  // 定义个体
	vector <double> namda;  // 定义个体对应的权重向量
	vector <int>    table;     // the vector for the indexes of neighboring subproblems  子问题领域向量表，存储的是
	// 距离最近的领域数量的向量索引值
	vector <int>    array;

    void  operator=(const TSOP&sub2);  // "="的运算符重载，实现个体的直接赋值的操作
};

TSOP::TSOP()
{
}

TSOP::~TSOP()
{
}


void TSOP::operator=(const TSOP&sub2)
{
    indiv  = sub2.indiv;
	table  = sub2.table;
	namda  = sub2.namda;
	array  = sub2.array;
}


#endif