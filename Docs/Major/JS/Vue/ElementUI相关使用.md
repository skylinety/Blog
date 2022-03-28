# ElementUI 相关使用

## Form 使用

### Form 校验

validate 函数回调不执行

```js
this.$refs[formName].validate((valid) => {
  if (valid) {
    console.log(' submit!!')
  } else {
    console.log('error submit!!')
    return false
  }
})
```

执行打印后，无相关打印信息。
出现这种问题的原因多为自定义校验规则的函数没有执行 callback 回调。

```js
var validatePassword = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('请输入密码')) // 检查
  } else {
    if (this.ruleForm.checkPass !== '') {
      this.$refs.ruleForm.validateField('checkPass')
    }
    callback() // 检查
  }
}
```

上述检查无问题，检查是否为 JSX 写法，JSX 写法下 model 传值不能如下

```js
<el-form
    class='info-form reset-el-form'
    label-position='top'
    label-width='80px'
    ref='ruleForm'
    model={this.params}
    v-model={this.params}
    rules={this.rules}
>
```

通过如上方式，无法将 model 值传入
![ElementUI相关使用20220314204155](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ElementUI%E7%9B%B8%E5%85%B3%E4%BD%BF%E7%94%A820220314204155.png)
将传值方式更改为 props 传值

```js
<el-form
    class='info-form reset-el-form'
    label-position='top'
    label-width='80px'
    ref='ruleForm'
    props={{
        model: this.params,
        rules: this.rules,
    }}
>
```

原因多在于 Vue 对于 JSX 语法支持的问题。

### Form 表单数字

可以通过以下方式来校验数字字段

```js
rules: {
  age: [
    {
      type: 'number',
      message: '请输入数字'
      transform: (value) => Number(value),
    }
  ]
},
```

若要校验数字长度，使用以下方式

```js
rules: {
  age: [
    {
      pattern: /\b\d{1,5}\b/,
      message: '请输入5位以下数字'
    }
  ]
},
```

## Dialog 使用

### 弹窗 X 点击不关闭

对于使用 JSX 语法的弹窗，由于不能直接使用.sync 修饰符，导致弹窗不能接收到传递属性变更的事件（update:visible）
在点击右上角关闭按钮时，弹窗无反应。
需要传递事件绑定属性

调整后如下

```js
<el-dialog
  class='reset-el-dialog reset-el-dialog__body '
  title='申请'
  on={{ 'update:visible': this.closeAll }}
  visible={this.dialogVisible}
  // {...{ on: { 'update:visible': console.log } }}
  // {...{ ['on-update:visible']: this.closeAll }}
  width='30%'
>
  {this.renderContent()}
</el-dialog>
```
