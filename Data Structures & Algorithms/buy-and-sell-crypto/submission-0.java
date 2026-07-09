class Solution {
    public int maxProfit(int[] prices) {
        int min = 1000; //dummy to declare first var min; 
        int profit = 0;
        if (prices.length == 1) {
            return 0; //base case in case the lenght is 1
        }
        for (int i = 0; i<prices.length; i++) {
            if (prices[i] < min) {
                min = prices[i]; //finds the min day to sell
            }
            else if (prices[i]-min>profit) {
                profit = prices[i]-min;
            }
        }
        return profit;
    }
}
