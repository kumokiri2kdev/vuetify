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

### 条件付きレンダリング
v-if ディレクティブ を使用すると、その条件が成立する場合のみエレメントが描画される。

```
<h1 v-if="awesome">Vue is awesome!</h1>
```
この場合、data の awesome の値が true の場合レンダリングされる。```this.awesome``` とは記述しなくていい。

v-else を使うと、v-if が成立しなかった時の記述ができる。
```
<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
```

v-else-if もある。

```
<div v-if="type === 'A'">
  A
</div>
<div v-else-if="type === 'B'">
  B
</div>
<div v-else-if="type === 'C'">
  C
</div>
<div v-else>
  Not A/B/C
</div>
```

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
