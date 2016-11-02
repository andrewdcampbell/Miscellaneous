import java.util.Random;

public class QuickSort {

	public static void main(String[] args) {
		Random r = new Random();
		int[] a = new int[100];
	    for (int i = 0; i < a.length; i++) {
	      a[i] = r.nextInt();
	    }
		quickSort(a, 0, a.length - 1);
		for (int i : a) {
			System.out.print(i + " ");
		}
		System.out.println();
	}

	public static void quickSort(int[] a, int lo, int hi) {
		if (lo >= hi) {
			return;
		}
		/* Partition */
		int pivot = a[(lo + hi) / 2];
		int l = lo;
		int r = hi;
		while (l <= r) {
			while (a[l] < pivot) {
				l++;
			}
			while (a[r] > pivot) {
				r--;
			}
			if (l <= r) {
				swap(a, l, r);
				l++;
				r--;
			}
		}
		/* Recursively sort partitions */
		quickSort(a, lo, r);
		quickSort(a, l, hi);
	}

	private static void swap(int[] a, int l, int r) {
		int temp = a[l];
		a[l] = a[r];
		a[r] = temp;
	}
}
