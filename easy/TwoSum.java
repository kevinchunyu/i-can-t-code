import java.util.*;
class TwoSum {
    public static void main(String[] args) {
        int[] array1 = {2,7,11,15};
        int target1 = 9;
        int[] result = twoSum(array1, target1);
        for(int i= 0; i < result.length; i++) {
            System.out.print(result[i]);
        }
    }

    public static int[] twoSum(int[] num, int target){
        Map<Integer, Integer> map1 = new HashMap<>();
        for(int i = 0; i < num.length; i++) {
            // put number in the array along with the index
            // have to put value first so we can get the output of the index later
            map1.put(num[i], i);
        }

        for(int i = 0; i < num.length; i++) {
            int complement = target - num[i];
            if(map1.containsKey(complement) && map1.get(complement) != i) {
                return new int[] {i, map1.get(complement)};
            }
        }
        return new int[] {};
    }
}