void swapNums(int &x, int &y){
	int z = x;
	x = y;
	y = z;
}

int main(){
	int firstNum = 10;
	int secondNum = 20;
  	swapNums(firstNum, secondNum);
	return 0;
}
