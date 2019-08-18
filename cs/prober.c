#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *bytes(void *p,int n){
  int i;
  int j;
  char *a = (char *) p;
  char *s = malloc(9*n+2);
  s[9*n] = '\n';
  s[9*n+1] = 0;


  j = 0;
  for(i=0;i< n*8;i++){
    s[j] = a[i/8] & (128 >> (i % 8)) ? '1' : '0';
    if (i% 8 == 7) { s[++j] = ' '; }
    ++j;
  }
  return s;
}

void printint(int a) {
  printf("%-8s %-5d: %s", "int", a, bytes(&a,sizeof(int)));
}

void printlong(long a) {
  printf("%-8s %-5d: %s", "long", a, bytes(&a,sizeof(long)));
}


void printstring(char *s) {
  printf("%-8s %-5s: %s", "string", s, bytes(s,strlen(s)+1));
}


void printfloat(float f) {
  printf("%-8s %-5.1f: %s", "float", f, bytes(&f,sizeof(float)));
}

void printdouble(double f) {
  printf("%-8s %-5.1f: %s", "double", f, bytes(&f,sizeof(double)));
}



int main(void) {
  
  printint(2);
  printint(4);
  printint(513);
  printlong(513);
  

  printint(-1);

  printint(-2);

  printstring("Hello");

  printstring("abcd");

  printfloat(33);
  printfloat(66);
  printfloat(132);
  printdouble(132);

  
  return 0;
}
