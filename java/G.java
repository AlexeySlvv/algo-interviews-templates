import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * G
 */
public class G {

    private static long getEnergyForUnion(List<Integer> stones) {
        // your code goes here
        return 0;
    }

    public static void main(String[] args) throws IOException {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
            int n = readInt(reader);
            List<Integer> stones = readList(reader);

            System.out.println(getEnergyForUnion(stones));
        } 
    }

    private static List<Integer> readList(BufferedReader reader) throws IOException {
        return Arrays.asList(reader.readLine().strip().split(" "))
            .stream()
            .map(token -> Integer.parseInt(token))
            .collect(Collectors.toList());
    }

    private static int readInt(BufferedReader reader) throws NumberFormatException, IOException {
        return Integer.parseInt(reader.readLine());
    } 
}