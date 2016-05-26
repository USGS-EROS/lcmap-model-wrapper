#include <stdlib.h>
#include <stdio.h>



int doubler (int x)
{
  return x * 2;
}

int tripler (int x)
{
  return x * 3;
}

int multiplier (int x, int y)
{
  return x * y;
}

int add(int red[], int green[], int blue[],  int count, int results[])
{
  // *results = (int *)malloc(sizeof(int *) * (count));
  for (int ix = 0; ix < count; ix++) {
    results[ix] = red[ix]+green[ix]+blue[ix];
  }
  return 0;
}

int main(int argc, char* argv[]) {
  printf("MyLib.\n");
  return 0;
}
