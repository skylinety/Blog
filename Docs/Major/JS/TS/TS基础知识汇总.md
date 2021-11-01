# TS 基础知识汇总

## class 实例属性可见性

class 实例通过 public、protected、private 来控制属性与方法的可用范围，类本生不可直接访问.
若要设置类自身属性，采用 static。
public 为默认值，任何位置，类和子类、类的实例都可访问。
protected 在类和子类中可用，实例化后不可用。
private 在类中可用，实例化和子类不可用。

```js
class Greeter {
  public greet() {
    console.log("Hello, " + this.getName() + this.getAge());
  }
  protected getName() {
    return "skyline";
  }
  private getAge() {
    return "18";
  }
}

class GreeterCN extends Greeter {
  public nihao() {
    console.log("你好, " + this.getName());
  }
}
const g = new GreeterCN();
g.greet();  //"Hello, skyline18"
g.nihao() // "你好, skyline"

```
