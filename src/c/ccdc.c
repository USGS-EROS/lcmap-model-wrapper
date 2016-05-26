#include <stdio.h>
#include <stdlib.h>
#include "ccdc.h"

void init(int red[], int green[], int blue[], char mask[], long times[], int *count, result **results)
{
  *count = 6;
  *results = (result *)(malloc(sizeof(result) * (*count)));
  for (int ix = 0; ix < *count; ix++) {
    (*results)[ix].start = (10*ix);
    (*results)[ix].stop  = (10*ix);
    (*results)[ix].c1 = (10*ix)+1;
    (*results)[ix].c2 = (10*ix)+2;
    (*results)[ix].c3 = (10*ix)+3;
  }
}

int main(int argc, char* argv[]) {
  /**
  printf("NDVI entry point.\n");
  printf("NDVI: %f", ndvi_double(1.0,2.0));

  printf("CCDC entry point.\n");

  int count = 0; // (int *)malloc(sizeof(int));
  result *results;

  init(0, 0, 0, 0, 0, &count, &results);

  printf("  count: %d\n",  count);
  for (int ix = 0; ix < count; ix++) {
    printf("*[%03d->%03d]\n", results[ix].start, results[ix].stop);
  }

  printf("CCDC finished.\n");
  */
  printf("CCDC.\n");
  return 0;
}
