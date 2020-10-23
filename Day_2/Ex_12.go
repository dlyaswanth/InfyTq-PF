//PF-Exer-12
//This verification is based on string match.

package main
import ("fmt")
func main(){
    //Write your program logic here
    var num1 int =3
    var num2 int =4
    var num3 int =1
    if (num1>num2){
        if (num1>num3){
            fmt.Println(num1);
        }else{
            fmt.Println(num3);
        }
    }else if (num2>num3){
        fmt.Println(num2);
    }else{
        fmt.Println(num3);
    }
}