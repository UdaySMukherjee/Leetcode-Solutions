class ParkingSystem {
    private int small;
    private int medium;
    private int big;

    public ParkingSystem(int big, int medium, int small) {
        this.big=big;
        this.medium=medium;
        this.small=small;
    }
    
    public boolean addCar(int carType) {
        if(carType==1){
            big--;
            return big>=0;
        }if(carType==2){
            medium--;
            return medium>=0;
        }else{
            small--;
            return small>=0;
        }
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */
