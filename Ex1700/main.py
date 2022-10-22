
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        starving = len(students)
        iter=0
        limit=len(students)*(len(students)+1)/2
        while(1):
            if iter>limit or len(students)==0 or len(sandwiches)==0: break
            if students[0]==sandwiches[0]:
                starving-=1
                sandwiches.pop(0)
            else:
                students.append(students[0])
            students.pop(0)
            iter+=1
        return starving
    
if __name__ == "__main__":
    print(Solution().countStudents([0,1,1,0], [1,1,0,0]))