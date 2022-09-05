#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum FORMAT {EMPTY, GREY, RGB, YCBCR, YCBCR420, BLOCK};

typedef struct {
	unsigned rows;
	unsigned cols;
	char format;
	unsigned long total;
	unsigned levels;
	short* content;

}ImageType;
typedef ImageType* Image;


Image imageAllocate(unsigned rows, unsigned cols, char format, unsigned levels) {
	Image im = malloc(sizeof(ImageType));
	im->rows = rows;
	im->cols = cols;
	im->format = format;
	im->levels = levels;
	im->content = NULL;

	if (im->format == EMPTY) {
		return im;
	}
	switch (im->format)
	{
	case GREY:
		im->total = im->cols * im->rows;
		break;
	case RGB:
		im->total = 3 * im->cols * im->rows;
		break;
	case YCBCR:
		im->total = 3 * im->cols * im->rows;
		break;
	case YCBCR420:
		im->total = 3 * im->cols * im->rows / 2;
		break;
	default:
		break;
	}
	im->content = malloc(im->total * sizeof(short));
	return im;
}

Image readPBMImage(const char* filename) {
	FILE* pgmFile;
	int k;

	char signature[3];
	unsigned cols, rows, levels;

	Image im = imageAllocate(0, 0, EMPTY, 0);

	pgmFile = fopen(filename, "rb");
	if (pgmFile == NULL) {
		perror("Cannot open file to read!");
		fclose(pgmFile);
		return imageAllocate(0, 0, EMPTY, 0);
	}
	fgets(signature, sizeof(signature), pgmFile);
	if (strcmp(signature, "P5") != 0 && strcmp(signature, "P6") != 0) {
		perror("Wrong file type!");
		fclose(pgmFile);
		return im;
	}

	fscanf(pgmFile, "%d %d %d", &cols, &rows, &levels);
	fgetc(pgmFile);

	if (strcmp(signature, "P5") == 0) {
		im = imageAllocate(rows, cols, GREY, levels);
		for (k = 0; k < im->total; ++k) {
			im->content[k] = (char)fgetc(pgmFile);
		}

	}
	else if (strcmp(signature, "P6") == 0) {
		im = imageAllocate(rows, cols, RGB, levels);
		unsigned long gOffset = im->cols * im->rows;
		unsigned long bOffset = 2 * im->cols * im->rows;
		for (k = 0; k < im->total / 3; ++k)
		{
			im->content[k] = (unsigned char)fgetc(pgmFile);
			im->content[k + gOffset] = (unsigned char)fgetc(pgmFile);
			im->content[k + bOffset] = (unsigned char)fgetc(pgmFile);

		}
	}

	fclose(pgmFile);
	return im;
}


void writePBMImage(const char* filename, const Image im) {
	FILE* pgmFile;
	int k;

	pgmFile = fopen(filename, "wb");
	if (pgmFile == NULL)
	{
		perror("Cannot open file to write");
		exit(EXIT_FAILURE);
	}
	if (im->format == GREY)
	{
		fprintf(pgmFile, "%s ", "P5");
	}
	else if (im->format == RGB) {
		fprintf(pgmFile, "%s ", "P6");
	}
	else {
		perror("Unknown file format\n");
		fclose(pgmFile);
		return;
	}

	fprintf(pgmFile, "%d %d", im->cols, im->rows);
	fprintf(pgmFile, "%d ", im->levels);

	if (im->format == GREY) {
		for (k = 0; k < im->total; ++k) {
			fputc((char)im->content[k], pgmFile);
		}
	}
	else if (im->format == RGB) {
		unsigned long gOffset = im->cols * im->rows;
		unsigned long bOffset = 2 * im->cols * im->rows;
		for (k = 0; k < im->total; ++k)
		{
			fputc((unsigned char)im->content[k], pgmFile);
			fputc((unsigned char)im->content[k + gOffset], pgmFile);
			fputc((unsigned char)im->content[k + bOffset], pgmFile);

		}
	}
	fclose(pgmFile);
}
void main() {
	Image a;
	a = readPBMImage("frog.pbm");
	writePBMImage("frog3.pbm", a);
}
