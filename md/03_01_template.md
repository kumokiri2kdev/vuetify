# テンプレート構文

## Mustache構文

### 基本形
```
<span>Message: {{ message }}</span>
```

このような記載において、アプリ側の

```
data: {
  message: 'Hello World'
}
```

の this.message が、HTML内で展開される。


### v-once ディレクティブ
```
<span v-once>This will never change: {{ message }}</span>
```
v-once ディレクティブを使用すると、データは一度だけ展開されるが、this.message が変わっても展開済みの HTML は変更されない。


[Basic Template](../examples/templates_sentence/basic_template.html)


## 属性
v-bind ディレクティブを使用する事で、html のエレメントの属性を変更することができる。

```
<div v-bind:id="dynamicId"></div>

<button v-bind:disabled="isButtonDisabled">Button</button>
```


## Java Script 式
Mustache構文 の中で、Java Script を使用することも可能。
ただし、単一の式のみ使用可能。

```
{{ number + 1 }}

{{ ok ? 'YES' : 'NO' }}

{{ message.split('').reverse().join('') }}

<div v-bind:id="'list-' + id"></div>
```
