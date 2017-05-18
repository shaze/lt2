
class Student { 


    String name;
    int      num_points;

    
    public Student (String name) {
	this.name=name;
    }


    public void addPoints (int num) {
	num_points += num;
    }

    
    public String toString() {
        return name + " has " + num_points + " points";
    }

}
