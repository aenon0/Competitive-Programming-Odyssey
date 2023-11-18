class Solution(object):
    def average(self, salary):
        repeated=0
        max_salary= float("-inf")
        min_salary= float("inf")
        sum= 0
        for individual_salary in salary:
           max_salary= max(max_salary, individual_salary)
           min_salary= min(min_salary, individual_salary)
           
        for individual_salary in salary:
            if individual_salary==max_salary:
                repeated+=1
            elif individual_salary==min_salary:
                repeated+=1
            else:
                sum+=individual_salary

        return sum/(len(salary)-repeated)
