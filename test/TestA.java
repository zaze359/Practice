package test;

public class TestA {

    interface IFace {
        int a = 0;
    }
    
    abstract class A {
        int a;
    }

    class B extends A implements IFace {
        void print() {
           int i =  IFace.a;
           i = ((A)this).a ;
        }
    }

    public static void main(String args[]) {

        int i = new Integer(10).intValue();
        System.out.println("i: " + i);
    }
}
