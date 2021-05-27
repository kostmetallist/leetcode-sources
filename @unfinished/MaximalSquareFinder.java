import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class MaximalSquareFinder {

    // TODO add possibility to work with rectangular matrices
    public static char[][] readMatrix(String path) {

        char[][] readResult = null;
        File file = new File(path);

        try (FileReader fr = new FileReader(file);
             BufferedReader br = new BufferedReader(fr)) {

            String line = br.readLine();
            if (line == null) {

                System.err.println("readMatrix: specified file is empty");
                readResult = null;
            }

            else {

                String[] elements = line.split(" ");
                int matrixSize = elements.length;
                readResult = new char[matrixSize][matrixSize];

                // processing first line individually, because it has
                // already been read by readLine method call
                for (int j = 0; j < matrixSize; ++j) {
                    readResult[0][j] = elements[j].charAt(0);
                }

                int lineNum = 1;
                while (lineNum < matrixSize && (line = br.readLine()) != null) {

                    elements = line.split(" ");
                    for (int j = 0; j < matrixSize; ++j) {
                        readResult[lineNum][j] = elements[j].charAt(0);
                    }

                    lineNum++;
                }
            }
        }

        catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        catch (IOException e) {
            e.printStackTrace();
        }

        return readResult;
    }
    
    // matrix is a 2-dimensional array consisting of 0 and 1
    public int maximalSquare(char[][] matrix) {
        
        System.out.println((int) matrix[1][1]);

        // TODO remove with valid return value
        return 0;
    }

    public static void main(String[] args) {

        Scanner inputScanner = new Scanner(System.in);
        System.out.print("Enter path to file with matrix: ");
        String fileName = inputScanner.nextLine();
        System.out.println("Opening " + fileName);

        char[][] matrix = readMatrix(fileName);
        if (matrix == null) {

            System.err.println("Empty matrix can't be processed");
            return;
        }

        int mRows = matrix.length, 
            mCols = matrix[0].length;

        // <printing out input file>
        for (int i = 0; i < mRows; ++i) {
            for (int j = 0; j < mCols; ++j) {
                System.out.print(matrix[i][j] + " ");
            }

            System.out.println();
        }
        // </printing out input file>

        // MaximalSquareFinder finder = new MaximalSquareFinder();
        // finder.maximalSquare(matrix);
    }
}