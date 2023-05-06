#include <stdio.h>

int main(int argc, char *argv[])
{
	int count = argc;

	printf("\nThe number of arguments passed is: [%d] \n", count);

	int c = 0;

	while(c < count)
	{
		printf("\nThe argument [%d] is: [%s]\n", c+1, argv[c]);
		c++;
	}
	printf("\nCode developed by Masino\n");
	return 0;
}
