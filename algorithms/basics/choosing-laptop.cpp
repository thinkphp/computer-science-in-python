#include<bits/stdc++.h>
using namespace std;
int n,x[111],y[111],z[111],cost[111];
int main()
{
	cin>>n;
	for(int i=0;i<n;i++)
		cin>>x[i]>>y[i]>>z[i]>>cost[i];
	int ans=-1;
	for(int i=0;i<n;i++){
		bool bad=false;
		for(int j=0;j<n;j++)
			if(x[i]<x[j]&&y[i]<y[j]&&z[i]<z[j])
				bad=true;
		if(!bad)
			if(ans==-1||cost[i]<cost[ans])
				ans=i;
	}
	cout<<ans+1<<endl;
	return 0;
}
