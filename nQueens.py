def safe(board,r,c):
    for  i in range(r):
      if board[i]==c or abs(board[i]-c) == abs(i-r):
         return False;
    return True

def nqueen(board,r,n):
   if r==n:
      print(board)
      return

   for c in range(n):
      if safe(board,r,c):
         board[r]=c
         nqueen(board,r+1,n)
         board[r]=-1

n=4
board = [-1]*n
nqueen(board,0,n)