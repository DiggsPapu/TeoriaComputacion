package Classes;

public class TwoValues<E,J> {
    protected E val1;
    protected J val2;

    public TwoValues() {
    }

    public TwoValues(E val1, J val2) {
        this.val1 = val1;
        this.val2 = val2;
    }

    public E getVal1() {
        return this.val1;
    }

    public void setVal1(E val1) {
        this.val1 = val1;
    }

    public J getVal2() {
        return this.val2;
    }

    public void setVal2(J val2) {
        this.val2 = val2;
    }

}
