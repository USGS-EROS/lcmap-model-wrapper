#include <stdio.h>
#include "index.h"

int ndvi_int(int nir, int vis) {
  return (nir-vis) / (nir+vis);
}

float ndvi_float(float nir, float vis) {
  return (nir-vis) / (nir+vis);
}

double ndvi_double(double nir, double vis) {
  return (nir-vis) / (nir+vis);
}

int main(int argc, char* argv[]) {
  printf("NDVI.\n");
  return 0;
}
