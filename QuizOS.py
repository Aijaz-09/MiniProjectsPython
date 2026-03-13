import random

print("**********************************************************"
      "\nRULES:"
      "\n   1)Every question carries 1 point."
      "\n   2)One wrong answer ----> GAME OVER"
      "\n**********************************************************")

print("\n")
q1 = "1. In Round Robin scheduling, the quantum size directly affects:\n A. Context switch overhead and response time\n B. Throughput only\n C. Deadlock probability\n D. Priority inversion"
a1 = 'A'

q2 = "2. Which of the following scheduling algorithms is optimal for minimizing average waiting time?\n A. FCFS\n B. SJF (non-preemptive)\n C. Priority Scheduling\n D. Round Robin"
a2 = "B"

q3 = "3. Which disk scheduling algorithm can cause the elevator effect?\n A. FCFS\n B. SSTF\n C. SCAN\n D. C-SCAN"
a3 = "C"

q4 = "4. SSTF (Shortest Seek Time First) may lead to:\n A. Starvation of requests far from the current head position\n B. Increased throughput compared to SCAN\n C. Guaranteed fairness\n D. Elimination of seek time"
a4 = "A"

q5 = "5. Which of the following is a deadlock prevention strategy?\n A. Allowing circular wait\n B. Imposing a total ordering on resource acquisition\n C. Ignoring deadlocks until they occur\n D. Using Banker's Algorithm"
a5 = "B"

q6 = "6. The Banker's Algorithm is used for:\n A. Deadlock detection\n B. Deadlock prevention\n C. Deadlock recovery\n D. Deadlock avoidance"
a6 = "D"

q7 = "7. In paging, the page table size depends on:\n A. Page size and logical address space\n B. Frame size and physical memory\n C. Both A and B\n D. None of the above"
a7 = "A"

q8 = "8. Segmentation provides:\n A. Fixed-size memory allocation\n B. Logical division of programs into variable-sized units\n C. Elimination of internal fragmentation\n D. Both B and C"
a8 = "D"

q9 = "9. User-level threads differ from kernel-level threads because:\n A. User-level threads require kernel support for scheduling\n B. Kernel-level threads are faster to create\n C. User-level threads are scheduled by a thread library, not the OS\n D. Kernel-level threads cannot run in parallel"
a9 = "C"

q10 = "10. In thread scheduling, priority inversion occurs when:\n A. A low-priority thread holds a resource needed by a high-priority thread\n B. A high-priority thread preempts a low-priority thread\n C. Threads are scheduled in round robin fashion\n D. Multiple threads share the same priority"
a10 = "A"

q11 = "11. A process may terminate due to all of the following except:\n A. Normal completion\n B. Parent termination\n C. Resource preemption\n D. Hardware failure"
a11 = "C"

q12 = "12. When a parent process terminates before its child, the child becomes:\n A. Zombie process\n B. Orphan process\n C. Suspended process\n D. Defunct process"
a12 = "B"
qna = {
      q1:a1,
      q2:a2,
      q3:a3,
      q4:a4,
      q5:a5,
      q6:a6,
      q7:a7,
      q8:a8,
      q9:a9,
      q10:a10,
      q11:a11,
      q12:a12
}

score = 0

for question, answer in qna.items():
      print("**********************************************************")
      print(question)
      userAns = str(input("Your Answer: "))
      if userAns.upper() != answer:
            print("WRONG ANSWER.....GAME OVER!")
            break
      else:
            print("CORRECT!")
            score = score + 1

print("\n**********************************************************")
print(f"SCORE: {score}")
print("THANKS FOR PLAYING! BE BACK SOON!")
print("**********************************************************")

