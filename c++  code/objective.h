#ifndef __OBJECTIVE_H_
#define __OBJECTIVE_H_

#include "global.h"

#define pi   3.1415926
#define SQR2  sqrt(2)

void objectives(vector<double> x_var, vector <double> &y_obj)
{

	//strcmp函数是string compare(字符串比较)的缩写，用于比较两个字符串并根据比较结果返回整数。基本形式为strcmp(str1,str2)，若str1=str2，
	//则返回零；若str1<str2，则返回负数；若str1>str2，则返回正数。
	if(!strcmp(strTestInstance,"ZDT1"))  // 实现ZDT1函数值的计算
	{
		double g = 0;
		for(int n=1;n<numVariables;n++)
			g+= x_var[n];
		g = 1 + 9*g/(numVariables-1);

		y_obj[0] = x_var[0];
		y_obj[1] = g*(1 - sqrt(y_obj[0]/g));
	}


	if(!strcmp(strTestInstance,"ZDT2"))
	{
		double g = 0;
		for(int n=1;n<numVariables;n++)
			g+= x_var[n];
		g = 1 + 9*g/(numVariables-1);
		y_obj[0] = x_var[0];
		y_obj[1] = g*(1 - pow(y_obj[0]/g,2));
	}


	
	if(!strcmp(strTestInstance,"ZDT3"))
	{
		double g = 0;
		for(int n=1;n<numVariables;n++)
			g+= x_var[n];
		g = 1 + 9*g/(numVariables-1);

		y_obj[0] = x_var[0];
		y_obj[1] = g*(1 - sqrt(x_var[0]/g) - x_var[0]*sin(10*pi*x_var[0])/g);
	}


	if(!strcmp(strTestInstance,"ZDT4"))
	{
		double g = 0;
		for(int n=1;n<numVariables;n++)
		{
			double x = 10*(x_var[n] - 0.5);
			g+= x*x - 10*cos(4*pi*x);
		}
		g = 1 + 10*(numVariables-1) + g;
		y_obj[0] = x_var[0];
		y_obj[1] = g*(1- sqrt(y_obj[0]/g));
	}

	if(!strcmp(strTestInstance,"ZDT6"))
	{
		double g = 0;
		for(int n=1;n<numVariables;n++)
			g+= x_var[n]/(numVariables - 1);
		g = 1 + 9*pow(g,0.25) ;

		y_obj[0] = 1 - exp(-4*x_var[0])*pow(sin(6*pi*x_var[0]),6);
		y_obj[1] = g*(1- pow(y_obj[0]/g,2));
	}

	// OKA 1
	if(!strcmp(strTestInstance,"OKA-1"))
	{
		double x1 = 2*pi*(x_var[0] - 0.5);
		double x2 = (x_var[1] - 0.5)*10;
		y_obj[0] = x1;
		y_obj[1] = pi - x1 + fabs(x2 - 5*cos(x1));
	}

	if(!strcmp(strTestInstance,"OKA-2"))
	{
		double x1 = 2*pow(pi,3)*(x_var[0] - 0.5);
		double x2 = (x_var[1] - 0.5)*10;
		double eta;
		if(x1>=0) eta = pow(x1,1.0/3);
		else      eta = -pow(-x1,1.0/3);

		y_obj[0] = eta;
		y_obj[1] = pi - eta + fabs(x2 - 5*cos(x1));
	}

	if(!strcmp(strTestInstance,"DTLZ1"))
	{
		double g = 0;
		for(int n=2; n<numVariables;n++)				
			g = g + pow(x_var[n]-0.5,2) - cos(20*pi*(x_var[n] - 0.5));
		g = 100*(numVariables- 2 + g);
		y_obj[0] = (1 + g)*x_var[0]*x_var[1];
		y_obj[1] = (1 + g)*x_var[0]*(1 - x_var[1]);
		y_obj[2] = (1 + g)*(1 - x_var[0]);
	}



	if(!strcmp(strTestInstance,"DTLZ2"))
	{
		double g = 0;
		double xx = (x_var[0] + x_var[1])/2.0;
		for(int n=2; n<numVariables;n++)				
		{
			double x = 2*(x_var[n] - 0.5);
			g = g + x*x;;
		}
		y_obj[0] = (1 + g)*cos(x_var[0]*pi/2)*cos(x_var[1]*pi/2);
		y_obj[1] = (1 + g)*cos(x_var[0]*pi/2)*sin(x_var[1]*pi/2);
		y_obj[2] = (1 + g)*sin(x_var[0]*pi/2);
	}

}


#endif