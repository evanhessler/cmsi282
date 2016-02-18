import java.util.HashMap;

public class CombinationComputerWithMemoization {
	private HashMap<String, Integer> cache = new HashMap<String, Integer>();

	public int nCr(int n, int r) {
		if (r == 0 || r == n) {
			return 1;
		} else if (cache.containsKey(Integer.toString(n) + " " + Integer.toString(r))) {
			return cache.get(Integer.toString(n) + " " + Integer.toString(r));
		} else {
			cache.put(Integer.toString(n) + " " + Integer.toString(r), nCr(n-1, r) + nCr(n-1, r-1));
			return cache.get(Integer.toString(n) + " " + Integer.toString(r));
		}
	}

	public static void main(String[] args) {
		CombinationComputerWithMemoization example = new CombinationComputerWithMemoization();
		example.nCr(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
	}
}
