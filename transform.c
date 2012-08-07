#define SIZE 128000

double transform() {
  double a = 2.0;
  double b = 0.5;
  double c = 0.1;
  double d = 0.5;
  double e = 2.0;
  double f = 0.1;

  double data[SIZE][2];

  double s = 0.0;

  for (int i = 0; i < SIZE; ++i) {
    double x = (double)i;
    double y = (double)i;

    double X = a*x + c*y + e;
    double Y = b*x + d*y + f;

    data[i][0] = X;
    data[i][1] = Y;

    s += X;
  }

  return s;
}
