class Solution
{
	int  select(int arr[], int i)
	{
        // code here such that selectionSort() sorts arr[]
        return i;
	}
	
	void selectionSort(int arr[], int n)
	{
	    //code here
	    int min,temp;
	    for (int i=0; i<n-1; i++){
	        min=select(arr, i);
	        arr[min]=arr[i];
	        for (int j=i+1; j<n; j++){
	            if (arr[j]<arr[min]){
	                min=j;
	            }
	        }
	        temp=arr[i];
	        arr[i]=arr[min];
	        arr[min]=temp;
	    }
	    
	    
	}
}
