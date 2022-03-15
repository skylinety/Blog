# ElementUI 相关使用

## Form 使用

### Form 校验问题

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

