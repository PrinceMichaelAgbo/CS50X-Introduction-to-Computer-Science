// Copies a BMP file

#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: n infile outfile\n");
        return 1;
    }
    float f = atof(argv[1]);
    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    if (f > 100.0 || f <= 0.0)
    {
        printf("Invalid Resize Factor.\nMust be positive and less than or equal to 100.0.\n");
        return 1;
    }


    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    int one = ftell(inptr);
    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);
    int two = ftell(inptr);

    // determine padding for scanlines for infile
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    fseek(inptr, (two - one) * -1, SEEK_CUR);
    // read infile's BITMAPFILEHEADER for outfile resizing
    BITMAPFILEHEADER bf2;
    fread(&bf2, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER for outfile Resizing
    BITMAPINFOHEADER bi2;
    fread(&bi2, sizeof(BITMAPINFOHEADER), 1, inptr);

    //Determine appropriate f
    if (f >= 1.0)

    {
        f = round(f);
    }
    else

    {
        f = 0.5;
    }

    if (bi.biWidth <= 1.0 || abs(bi.biHeight) <= 1.0)

    {
        f = 1.0;
        printf("%i\n", bi.biWidth);
        printf("%i\n", bi.biHeight);
    }

    //header/padding updates for resizing
    bi2.biWidth *= f;
    bi2.biHeight *= f;
    int padding2 = (4 - (bi2.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    bi2.biSizeImage = ((sizeof(RGBTRIPLE) * bi2.biWidth) + padding2) * abs(bi2.biHeight);
    bf2.bfSize = bi2.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf2, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi2, sizeof(BITMAPINFOHEADER), 1, outptr);


    // iterate over infile's scanlines
    if (f >= 1.0)

    {
        for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
        {
            for (int m = 1; m < f; m++)
            {
                int start = ftell(inptr);
                // iterate over pixels in scanline
                for (int j = 0; j < bi.biWidth; j++)
                {
                    // temporary storage
                    RGBTRIPLE triple;

                    // read RGB triple from infile
                    fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                    // write RGB triple to outfile
                    for (int k = 0; k < f; k++)
                    {
                        fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                    }

                }
                int end = ftell(inptr);
                //write outfile's padding
                for (int k = 0; k < padding2; k++)
                {
                    fputc(0x00, outptr);
                }
                fseek(inptr, (end - start) * -1, SEEK_CUR);
            }

            for (int j = 0; j < bi.biWidth; j++)
            {
                // temporary storage
                RGBTRIPLE triple;

                // read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                // write RGB triple to outfile

                for (int k = 0; k < f; k++)
                {
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                }

            }
            for (int k = 0; k < padding2; k++)

            {
                fputc(0x00, outptr);
            }
            // skip over infile padding, if any
            fseek(inptr, padding, SEEK_CUR);
        }
    }
    else
    {
        int counterRow = 0;
        int counterHeight = 0;
        for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)

        {
            if (counterHeight % 2 == 0)

            {
                for (int j = 0; j < bi.biWidth; j++)

                {
                    // temporary storage
                    RGBTRIPLE triple;

                    // read RGB triple from infile
                    fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                    // write RGB triple to outfile
                    if (counterRow % 2 == 0)

                    {
                        fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                    }
                    counterRow += 1;
                }
                for (int k = 0; k < padding2; k++)
                {
                    fputc(0x00, outptr);
                }
                // skip over infile padding, if any
                fseek(inptr, padding, SEEK_CUR);
            }
            else

            {
                for (int m = 0; m < bi.biWidth; m++)

                {
                    // temporary storage
                    RGBTRIPLE triple;

                    // read RGB triple from infile
                    fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                }
                // skip over infile padding, if any
                fseek(inptr, padding, SEEK_CUR);
            }
            counterHeight += 1;
        }
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
