(function(){'use strict';var m;function aa(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
var ba="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
function ca(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("Cannot find global object");}
var fa=ca(this);function u(a,b){if(b)a:{var c=fa;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&ba(c,a,{configurable:!0,writable:!0,value:b})}}
u("Symbol",function(a){function b(f){if(this instanceof b)throw new TypeError("Symbol is not a constructor");return new c(d+(f||"")+"_"+e++,f)}
function c(f,g){this.h=f;ba(this,"description",{configurable:!0,writable:!0,value:g})}
if(a)return a;c.prototype.toString=function(){return this.h};
var d="jscomp_symbol_"+(1E9*Math.random()>>>0)+"_",e=0;return b});
u("Symbol.iterator",function(a){if(a)return a;a=Symbol("Symbol.iterator");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=fa[b[c]];"function"===typeof d&&"function"!=typeof d.prototype[a]&&ba(d.prototype,a,{configurable:!0,writable:!0,value:function(){return ia(aa(this))}})}return a});
function ia(a){a={next:a};a[Symbol.iterator]=function(){return this};
return a}
function ja(a){return a.raw=a}
function ka(a,b){a.raw=b;return a}
function x(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];if(b)return b.call(a);if("number"==typeof a.length)return{next:aa(a)};throw Error(String(a)+" is not an iterable or ArrayLike");}
function la(a){if(!(a instanceof Array)){a=x(a);for(var b,c=[];!(b=a.next()).done;)c.push(b.value);a=c}return a}
function ma(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
var oa="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)ma(d,e)&&(a[e]=d[e])}return a};
u("Object.assign",function(a){return a||oa});
var pa="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},qa=function(){function a(){function c(){}
new c;Reflect.construct(c,[],function(){});
return new c instanceof c}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(c,d,e){c=b(c,d);e&&Reflect.setPrototypeOf(c,e.prototype);return c}}return function(c,d,e){void 0===e&&(e=c);
e=pa(e.prototype||Object.prototype);return Function.prototype.apply.call(c,e,d)||e}}(),ra;
if("function"==typeof Object.setPrototypeOf)ra=Object.setPrototypeOf;else{var sa;a:{var ua={a:!0},va={};try{va.__proto__=ua;sa=va.a;break a}catch(a){}sa=!1}ra=sa?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var wa=ra;
function y(a,b){a.prototype=pa(b.prototype);a.prototype.constructor=a;if(wa)wa(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.Ba=b.prototype}
function xa(){this.A=!1;this.m=null;this.i=void 0;this.h=1;this.v=this.l=0;this.K=this.j=null}
function ya(a){if(a.A)throw new TypeError("Generator is already running");a.A=!0}
xa.prototype.F=function(a){this.i=a};
function za(a,b){a.j={exception:b,jd:!0};a.h=a.l||a.v}
xa.prototype.return=function(a){this.j={return:a};this.h=this.v};
xa.prototype.yield=function(a,b){this.h=b;return{value:a}};
xa.prototype.B=function(a){this.h=a};
function Aa(a,b,c){a.l=b;void 0!=c&&(a.v=c)}
function Ba(a){a.l=0;var b=a.j.exception;a.j=null;return b}
function Ca(a){var b=a.K.splice(0)[0];(b=a.j=a.j||b)?b.jd?a.h=a.l||a.v:void 0!=b.B&&a.v<b.B?(a.h=b.B,a.j=null):a.h=a.v:a.h=0}
function Da(a){this.h=new xa;this.i=a}
function Ea(a,b){ya(a.h);var c=a.h.m;if(c)return Fa(a,"return"in c?c["return"]:function(d){return{value:d,done:!0}},b,a.h.return);
a.h.return(b);return Ga(a)}
function Fa(a,b,c,d){try{var e=b.call(a.h.m,c);if(!(e instanceof Object))throw new TypeError("Iterator result "+e+" is not an object");if(!e.done)return a.h.A=!1,e;var f=e.value}catch(g){return a.h.m=null,za(a.h,g),Ga(a)}a.h.m=null;d.call(a.h,f);return Ga(a)}
function Ga(a){for(;a.h.h;)try{var b=a.i(a.h);if(b)return a.h.A=!1,{value:b.value,done:!1}}catch(c){a.h.i=void 0,za(a.h,c)}a.h.A=!1;if(a.h.j){b=a.h.j;a.h.j=null;if(b.jd)throw b.exception;return{value:b.return,done:!0}}return{value:void 0,done:!0}}
function Ha(a){this.next=function(b){ya(a.h);a.h.m?b=Fa(a,a.h.m.next,b,a.h.F):(a.h.F(b),b=Ga(a));return b};
this.throw=function(b){ya(a.h);a.h.m?b=Fa(a,a.h.m["throw"],b,a.h.F):(za(a.h,b),b=Ga(a));return b};
this.return=function(b){return Ea(a,b)};
this[Symbol.iterator]=function(){return this}}
function Ia(a){function b(d){return a.next(d)}
function c(d){return a.throw(d)}
return new Promise(function(d,e){function f(g){g.done?d(g.value):Promise.resolve(g.value).then(b,c).then(f,e)}
f(a.next())})}
function z(a){return Ia(new Ha(new Da(a)))}
function A(){for(var a=Number(this),b=[],c=a;c<arguments.length;c++)b[c-a]=arguments[c];return b}
u("Reflect",function(a){return a?a:{}});
u("Reflect.construct",function(){return qa});
u("Reflect.setPrototypeOf",function(a){return a?a:wa?function(b,c){try{return wa(b,c),!0}catch(d){return!1}}:null});
u("Promise",function(a){function b(g){this.h=0;this.j=void 0;this.i=[];this.A=!1;var h=this.l();try{g(h.resolve,h.reject)}catch(k){h.reject(k)}}
function c(){this.h=null}
function d(g){return g instanceof b?g:new b(function(h){h(g)})}
if(a)return a;c.prototype.i=function(g){if(null==this.h){this.h=[];var h=this;this.j(function(){h.v()})}this.h.push(g)};
var e=fa.setTimeout;c.prototype.j=function(g){e(g,0)};
c.prototype.v=function(){for(;this.h&&this.h.length;){var g=this.h;this.h=[];for(var h=0;h<g.length;++h){var k=g[h];g[h]=null;try{k()}catch(l){this.l(l)}}}this.h=null};
c.prototype.l=function(g){this.j(function(){throw g;})};
b.prototype.l=function(){function g(l){return function(n){k||(k=!0,l.call(h,n))}}
var h=this,k=!1;return{resolve:g(this.da),reject:g(this.v)}};
b.prototype.da=function(g){if(g===this)this.v(new TypeError("A Promise cannot resolve to itself"));else if(g instanceof b)this.ja(g);else{a:switch(typeof g){case "object":var h=null!=g;break a;case "function":h=!0;break a;default:h=!1}h?this.ba(g):this.m(g)}};
b.prototype.ba=function(g){var h=void 0;try{h=g.then}catch(k){this.v(k);return}"function"==typeof h?this.xa(h,g):this.m(g)};
b.prototype.v=function(g){this.F(2,g)};
b.prototype.m=function(g){this.F(1,g)};
b.prototype.F=function(g,h){if(0!=this.h)throw Error("Cannot settle("+g+", "+h+"): Promise already settled in state"+this.h);this.h=g;this.j=h;2===this.h&&this.ga();this.K()};
b.prototype.ga=function(){var g=this;e(function(){if(g.W()){var h=fa.console;"undefined"!==typeof h&&h.error(g.j)}},1)};
b.prototype.W=function(){if(this.A)return!1;var g=fa.CustomEvent,h=fa.Event,k=fa.dispatchEvent;if("undefined"===typeof k)return!0;"function"===typeof g?g=new g("unhandledrejection",{cancelable:!0}):"function"===typeof h?g=new h("unhandledrejection",{cancelable:!0}):(g=fa.document.createEvent("CustomEvent"),g.initCustomEvent("unhandledrejection",!1,!0,g));g.promise=this;g.reason=this.j;return k(g)};
b.prototype.K=function(){if(null!=this.i){for(var g=0;g<this.i.length;++g)f.i(this.i[g]);this.i=null}};
var f=new c;b.prototype.ja=function(g){var h=this.l();g.ac(h.resolve,h.reject)};
b.prototype.xa=function(g,h){var k=this.l();try{g.call(h,k.resolve,k.reject)}catch(l){k.reject(l)}};
b.prototype.then=function(g,h){function k(r,t){return"function"==typeof r?function(v){try{l(r(v))}catch(w){n(w)}}:t}
var l,n,p=new b(function(r,t){l=r;n=t});
this.ac(k(g,l),k(h,n));return p};
b.prototype.catch=function(g){return this.then(void 0,g)};
b.prototype.ac=function(g,h){function k(){switch(l.h){case 1:g(l.j);break;case 2:h(l.j);break;default:throw Error("Unexpected state: "+l.h);}}
var l=this;null==this.i?f.i(k):this.i.push(k);this.A=!0};
b.resolve=d;b.reject=function(g){return new b(function(h,k){k(g)})};
b.race=function(g){return new b(function(h,k){for(var l=x(g),n=l.next();!n.done;n=l.next())d(n.value).ac(h,k)})};
b.all=function(g){var h=x(g),k=h.next();return k.done?d([]):new b(function(l,n){function p(v){return function(w){r[v]=w;t--;0==t&&l(r)}}
var r=[],t=0;do r.push(void 0),t++,d(k.value).ac(p(r.length-1),n),k=h.next();while(!k.done)})};
return b});
u("Object.setPrototypeOf",function(a){return a||wa});
u("WeakMap",function(a){function b(k){this.h=(h+=Math.random()+1).toString();if(k){k=x(k);for(var l;!(l=k.next()).done;)l=l.value,this.set(l[0],l[1])}}
function c(){}
function d(k){var l=typeof k;return"object"===l&&null!==k||"function"===l}
function e(k){if(!ma(k,g)){var l=new c;ba(k,g,{value:l})}}
function f(k){var l=Object[k];l&&(Object[k]=function(n){if(n instanceof c)return n;Object.isExtensible(n)&&e(n);return l(n)})}
if(function(){if(!a||!Object.seal)return!1;try{var k=Object.seal({}),l=Object.seal({}),n=new a([[k,2],[l,3]]);if(2!=n.get(k)||3!=n.get(l))return!1;n.delete(k);n.set(l,4);return!n.has(k)&&4==n.get(l)}catch(p){return!1}}())return a;
var g="$jscomp_hidden_"+Math.random();f("freeze");f("preventExtensions");f("seal");var h=0;b.prototype.set=function(k,l){if(!d(k))throw Error("Invalid WeakMap key");e(k);if(!ma(k,g))throw Error("WeakMap key fail: "+k);k[g][this.h]=l;return this};
b.prototype.get=function(k){return d(k)&&ma(k,g)?k[g][this.h]:void 0};
b.prototype.has=function(k){return d(k)&&ma(k,g)&&ma(k[g],this.h)};
b.prototype.delete=function(k){return d(k)&&ma(k,g)&&ma(k[g],this.h)?delete k[g][this.h]:!1};
return b});
u("Map",function(a){function b(){var h={};return h.previous=h.next=h.head=h}
function c(h,k){var l=h[1];return ia(function(){if(l){for(;l.head!=h[1];)l=l.previous;for(;l.next!=l.head;)return l=l.next,{done:!1,value:k(l)};l=null}return{done:!0,value:void 0}})}
function d(h,k){var l=k&&typeof k;"object"==l||"function"==l?f.has(k)?l=f.get(k):(l=""+ ++g,f.set(k,l)):l="p_"+k;var n=h[0][l];if(n&&ma(h[0],l))for(h=0;h<n.length;h++){var p=n[h];if(k!==k&&p.key!==p.key||k===p.key)return{id:l,list:n,index:h,entry:p}}return{id:l,list:n,index:-1,entry:void 0}}
function e(h){this[0]={};this[1]=b();this.size=0;if(h){h=x(h);for(var k;!(k=h.next()).done;)k=k.value,this.set(k[0],k[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var h=Object.seal({x:4}),k=new a(x([[h,"s"]]));if("s"!=k.get(h)||1!=k.size||k.get({x:4})||k.set({x:4},"t")!=k||2!=k.size)return!1;var l=k.entries(),n=l.next();if(n.done||n.value[0]!=h||"s"!=n.value[1])return!1;n=l.next();return n.done||4!=n.value[0].x||"t"!=n.value[1]||!l.next().done?!1:!0}catch(p){return!1}}())return a;
var f=new WeakMap;e.prototype.set=function(h,k){h=0===h?0:h;var l=d(this,h);l.list||(l.list=this[0][l.id]=[]);l.entry?l.entry.value=k:(l.entry={next:this[1],previous:this[1].previous,head:this[1],key:h,value:k},l.list.push(l.entry),this[1].previous.next=l.entry,this[1].previous=l.entry,this.size++);return this};
e.prototype.delete=function(h){h=d(this,h);return h.entry&&h.list?(h.list.splice(h.index,1),h.list.length||delete this[0][h.id],h.entry.previous.next=h.entry.next,h.entry.next.previous=h.entry.previous,h.entry.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this[0]={};this[1]=this[1].previous=b();this.size=0};
e.prototype.has=function(h){return!!d(this,h).entry};
e.prototype.get=function(h){return(h=d(this,h).entry)&&h.value};
e.prototype.entries=function(){return c(this,function(h){return[h.key,h.value]})};
e.prototype.keys=function(){return c(this,function(h){return h.key})};
e.prototype.values=function(){return c(this,function(h){return h.value})};
e.prototype.forEach=function(h,k){for(var l=this.entries(),n;!(n=l.next()).done;)n=n.value,h.call(k,n[1],n[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
function Ja(a,b,c){if(null==a)throw new TypeError("The 'this' value for String.prototype."+c+" must not be null or undefined");if(b instanceof RegExp)throw new TypeError("First argument to String.prototype."+c+" must not be a regular expression");return a+""}
u("String.prototype.endsWith",function(a){return a?a:function(b,c){var d=Ja(this,b,"endsWith");b+="";void 0===c&&(c=d.length);c=Math.max(0,Math.min(c|0,d.length));for(var e=b.length;0<e&&0<c;)if(d[--c]!=b[--e])return!1;return 0>=e}});
function Ma(a,b){a instanceof String&&(a+="");var c=0,d=!1,e={next:function(){if(!d&&c<a.length){var f=c++;return{value:b(f,a[f]),done:!1}}d=!0;return{done:!0,value:void 0}}};
e[Symbol.iterator]=function(){return e};
return e}
u("Array.prototype.entries",function(a){return a?a:function(){return Ma(this,function(b,c){return[b,c]})}});
u("Array.prototype.keys",function(a){return a?a:function(){return Ma(this,function(b){return b})}});
u("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=Ja(this,b,"startsWith");b+="";var e=d.length,f=b.length;c=Math.max(0,Math.min(c|0,d.length));for(var g=0;g<f&&c<e;)if(d[c++]!=b[g++])return!1;return g>=f}});
u("Number.isFinite",function(a){return a?a:function(b){return"number"!==typeof b?!1:!isNaN(b)&&Infinity!==b&&-Infinity!==b}});
u("Array.prototype.find",function(a){return a?a:function(b,c){a:{var d=this;d instanceof String&&(d=String(d));for(var e=d.length,f=0;f<e;f++){var g=d[f];if(b.call(c,g,f,d)){b=g;break a}}b=void 0}return b}});
u("Set",function(a){function b(c){this.h=new Map;if(c){c=x(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.h.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var c=Object.seal({x:4}),d=new a(x([c]));if(!d.has(c)||1!=d.size||d.add(c)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=c||f.value[1]!=c)return!1;f=e.next();return f.done||f.value[0]==c||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
b.prototype.add=function(c){c=0===c?0:c;this.h.set(c,c);this.size=this.h.size;return this};
b.prototype.delete=function(c){c=this.h.delete(c);this.size=this.h.size;return c};
b.prototype.clear=function(){this.h.clear();this.size=0};
b.prototype.has=function(c){return this.h.has(c)};
b.prototype.entries=function(){return this.h.entries()};
b.prototype.values=function(){return this.h.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.h.forEach(function(f){return c.call(d,f,f,e)})};
return b});
u("Array.prototype.values",function(a){return a?a:function(){return Ma(this,function(b,c){return c})}});
u("Number.MAX_SAFE_INTEGER",function(){return 9007199254740991});
u("Number.isInteger",function(a){return a?a:function(b){return Number.isFinite(b)?b===Math.floor(b):!1}});
u("Number.isSafeInteger",function(a){return a?a:function(b){return Number.isInteger(b)&&Math.abs(b)<=Number.MAX_SAFE_INTEGER}});
u("Math.trunc",function(a){return a?a:function(b){b=Number(b);if(isNaN(b)||Infinity===b||-Infinity===b||0===b)return b;var c=Math.floor(Math.abs(b));return 0>b?-c:c}});
u("Object.values",function(a){return a?a:function(b){var c=[],d;for(d in b)ma(b,d)&&c.push(b[d]);return c}});
u("Object.is",function(a){return a?a:function(b,c){return b===c?0!==b||1/b===1/c:b!==b&&c!==c}});
u("Array.prototype.includes",function(a){return a?a:function(b,c){var d=this;d instanceof String&&(d=String(d));var e=d.length;c=c||0;for(0>c&&(c=Math.max(c+e,0));c<e;c++){var f=d[c];if(f===b||Object.is(f,b))return!0}return!1}});
u("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==Ja(this,b,"includes").indexOf(b,c||0)}});
u("Number.isNaN",function(a){return a?a:function(b){return"number"===typeof b&&isNaN(b)}});
u("Array.from",function(a){return a?a:function(b,c,d){c=null!=c?c:function(h){return h};
var e=[],f="undefined"!=typeof Symbol&&Symbol.iterator&&b[Symbol.iterator];if("function"==typeof f){b=f.call(b);for(var g=0;!(f=b.next()).done;)e.push(c.call(d,f.value,g++))}else for(f=b.length,g=0;g<f;g++)e.push(c.call(d,b[g],g));return e}});
u("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)ma(b,d)&&c.push([d,b[d]]);return c}});
u("globalThis",function(a){return a||fa});/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var Na=Na||{},B=this||self;function D(a,b,c){a=a.split(".");c=c||B;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
function Oa(a){var b=E("CLOSURE_FLAGS");a=b&&b[a];return null!=a?a:!1}
function E(a,b){a=a.split(".");b=b||B;for(var c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function Pa(a){var b=typeof a;return"object"!=b?b:a?Array.isArray(a)?"array":b:"null"}
function Qa(a){var b=Pa(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function Ra(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function Sa(a){return Object.prototype.hasOwnProperty.call(a,Ta)&&a[Ta]||(a[Ta]=++Ua)}
var Ta="closure_uid_"+(1E9*Math.random()>>>0),Ua=0;function Va(a,b,c){return a.call.apply(a.bind,arguments)}
function Wa(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}}
function Xa(a,b,c){Xa=Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?Va:Wa;return Xa.apply(null,arguments)}
function Ya(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}}
function Za(){return Date.now()}
function $a(a,b){function c(){}
c.prototype=b.prototype;a.Ba=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.base=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}}
function ab(a){return a}
;function bb(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,bb);else{var c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));void 0!==b&&(this.cause=b)}
$a(bb,Error);bb.prototype.name="CustomError";function cb(a){a=a.url;var b=/[?&]dsh=1(&|$)/.test(a);this.j=!b&&/[?&]ae=1(&|$)/.test(a);this.l=!b&&/[?&]ae=2(&|$)/.test(a);if((this.h=/[?&]adurl=([^&]*)/.exec(a))&&this.h[1]){try{var c=decodeURIComponent(this.h[1])}catch(d){c=null}this.i=c}}
;var db=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};var eb;function fb(){if(void 0===eb){var a=null,b=B.trustedTypes;if(b&&b.createPolicy){try{a=b.createPolicy("goog#html",{createHTML:ab,createScript:ab,createScriptURL:ab})}catch(c){B.console&&B.console.error(c.message)}eb=a}else eb=a}return eb}
;function gb(a,b){this.h=a===hb&&b||""}
gb.prototype.toString=function(){return this.h};
function ib(a){return new gb(hb,a)}
var hb={};ib("");function jb(a){this.h=a}
jb.prototype.toString=function(){return this.h+""};
function kb(a){if(a instanceof jb&&a.constructor===jb)return a.h;Pa(a);return"type_error:TrustedResourceUrl"}
var lb={};function mb(a){var b=fb();a=b?b.createScriptURL(a):a;return new jb(a,lb)}
;/*

 SPDX-License-Identifier: Apache-2.0
*/
var nb=ja([""]),ob=ka(["\x00"],["\\0"]),pb=ka(["\n"],["\\n"]),qb=ka(["\x00"],["\\u0000"]);function rb(a){return-1===a.toString().indexOf("`")}
rb(function(a){return a(nb)})||rb(function(a){return a(ob)})||rb(function(a){return a(pb)})||rb(function(a){return a(qb)});function sb(a){this.h=a}
sb.prototype.toString=function(){return this.h};
var tb=new sb("about:invalid#zClosurez");function ub(a){this.qe=a}
function vb(a){return new ub(function(b){return b.substr(0,a.length+1).toLowerCase()===a+":"})}
var wb=[vb("data"),vb("http"),vb("https"),vb("mailto"),vb("ftp"),new ub(function(a){return/^[^:]*([/?#]|$)/.test(a)})],xb=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;
function yb(a){if(a instanceof sb)if(a instanceof sb)a=a.h;else throw Error("");else a=xb.test(a)?a:void 0;return a}
;function zb(a,b){b=yb(b);void 0!==b&&(a.href=b)}
;function Ab(){this.h=Bb[0].toLowerCase()}
Ab.prototype.toString=function(){return this.h};var Cb=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},Db=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},Eb=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f="string"===typeof a?a.split(""):a,g=0;g<c;g++)if(g in f){var h=f[g];
b.call(void 0,h,g,a)&&(d[e++]=h)}return d},Fb=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e="string"===typeof a?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d},Gb=Array.prototype.reduce?function(a,b,c){return Array.prototype.reduce.call(a,b,c)}:function(a,b,c){var d=c;
Db(a,function(e,f){d=b.call(void 0,d,e,f,a)});
return d};
function Hb(a,b){a:{for(var c=a.length,d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){b=e;break a}b=-1}return 0>b?null:"string"===typeof a?a.charAt(b):a[b]}
function Ib(a,b){b=Cb(a,b);var c;(c=0<=b)&&Array.prototype.splice.call(a,b,1);return c}
function Jb(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(Qa(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;function Kb(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function Lb(a){var b=Mb,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function Nb(a){for(var b in a)return!1;return!0}
function Ob(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function Pb(a){return null!==a&&"privembed"in a?a.privembed:!1}
function Qb(a,b){for(var c in a)if(!(c in b)||a[c]!==b[c])return!1;for(var d in b)if(!(d in a))return!1;return!0}
function Rb(a){var b={},c;for(c in a)b[c]=a[c];return b}
function Sb(a){if(!a||"object"!==typeof a)return a;if("function"===typeof a.clone)return a.clone();if("undefined"!==typeof Map&&a instanceof Map)return new Map(a);if("undefined"!==typeof Set&&a instanceof Set)return new Set(a);if(a instanceof Date)return new Date(a.getTime());var b=Array.isArray(a)?[]:"function"!==typeof ArrayBuffer||"function"!==typeof ArrayBuffer.isView||!ArrayBuffer.isView(a)||a instanceof DataView?{}:new a.constructor(a.length),c;for(c in a)b[c]=Sb(a[c]);return b}
var Tb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function Ub(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<Tb.length;f++)c=Tb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;function Vb(a){this.h=a}
Vb.prototype.toString=function(){return this.h.toString()};function Wb(a){var b="true".toString(),c=[new Ab];if(0===c.length)throw Error("");if(c.map(function(d){if(d instanceof Ab)d=d.h;else throw Error("");return d}).every(function(d){return 0!=="data-loaded".indexOf(d)}))throw Error('Attribute "data-loaded" does not match any of the allowed prefixes.');
a.setAttribute("data-loaded",b)}
;function Xb(a,b){throw Error(void 0===b?"unexpected value "+a+"!":b);}
;var Yb="alternate author bookmark canonical cite help icon license modulepreload next prefetch dns-prefetch prerender preconnect preload prev search subresource".split(" ");function Zb(a,b){if(b instanceof jb)a.href=kb(b).toString();else{if(-1===Yb.indexOf("stylesheet"))throw Error('TrustedResourceUrl href attribute required with rel="stylesheet"');b=yb(b);if(void 0===b)return;a.href=b}a.rel="stylesheet"}
;function $b(a){var b,c;return(a=null==(c=(b=a.document).querySelector)?void 0:c.call(b,"script[nonce]"))?a.nonce||a.getAttribute("nonce")||"":""}
;function ac(a){this.h=a}
ac.prototype.toString=function(){return this.h.toString()};function bc(a){var b=$b(a.ownerDocument&&a.ownerDocument.defaultView||window);b&&a.setAttribute("nonce",b)}
function cc(a,b){if(b instanceof ac)b=b.h;else throw Error("");a.textContent=b;bc(a)}
function dc(a,b){a.src=kb(b);bc(a)}
;function ec(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b}
;function fc(a){var b=E("window.location.href");null==a&&(a='Unknown Error of type "null/undefined"');if("string"===typeof a)return{message:a,name:"Unknown error",lineNumber:"Not available",fileName:b,stack:"Not available"};var c=!1;try{var d=a.lineNumber||a.line||"Not available"}catch(g){d="Not available",c=!0}try{var e=a.fileName||a.filename||a.sourceURL||B.$googDebugFname||b}catch(g){e="Not available",c=!0}b=hc(a);if(!(!c&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name)){c=a.message;if(null==
c){if(a.constructor&&a.constructor instanceof Function){if(a.constructor.name)c=a.constructor.name;else if(c=a.constructor,ic[c])c=ic[c];else{c=String(c);if(!ic[c]){var f=/function\s+([^\(]+)/m.exec(c);ic[c]=f?f[1]:"[Anonymous]"}c=ic[c]}c='Unknown Error of type "'+c+'"'}else c="Unknown Error of unknown type";"function"===typeof a.toString&&Object.prototype.toString!==a.toString&&(c+=": "+a.toString())}return{message:c,name:a.name||"UnknownError",lineNumber:d,fileName:e,stack:b||"Not available"}}return{message:a.message,
name:a.name,lineNumber:a.lineNumber,fileName:a.fileName,stack:b}}
function hc(a,b){b||(b={});b[jc(a)]=!0;var c=a.stack||"";(a=a.cause)&&!b[jc(a)]&&(c+="\nCaused by: ",a.stack&&0==a.stack.indexOf(a.toString())||(c+="string"===typeof a?a:a.message+"\n"),c+=hc(a,b));return c}
function jc(a){var b="";"function"===typeof a.toString&&(b=""+a);return b+a.stack}
var ic={};function kc(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var lc=RegExp("^(?:([^:/?#.]+):)?(?://(?:([^\\\\/?#]*)@)?([^\\\\/?#]*?)(?::([0-9]+))?(?=[\\\\/?#]|$))?([^?#]+)?(?:\\?([^#]*))?(?:#([\\s\\S]*))?$");function mc(a){return a?decodeURI(a):a}
function nc(a,b){return b.match(lc)[a]||null}
function oc(a){return mc(nc(3,a))}
function pc(a){var b=a.match(lc);a=b[5];var c=b[6];b=b[7];var d="";a&&(d+=a);c&&(d+="?"+c);b&&(d+="#"+b);return d}
function qc(a){var b=a.indexOf("#");return 0>b?a:a.slice(0,b)}
function rc(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)rc(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function sc(a){var b=[],c;for(c in a)rc(c,a[c],b);return b.join("&")}
function tc(a,b){b=sc(b);if(b){var c=a.indexOf("#");0>c&&(c=a.length);var d=a.indexOf("?");if(0>d||d>c){d=c;var e=""}else e=a.substring(d+1,c);a=[a.slice(0,d),e,a.slice(c)];c=a[1];a[1]=b?c?c+"&"+b:b:c;b=a[0]+(a[1]?"?"+a[1]:"")+a[2]}else b=a;return b}
function uc(a,b,c,d){for(var e=c.length;0<=(b=a.indexOf(c,b))&&b<d;){var f=a.charCodeAt(b-1);if(38==f||63==f)if(f=a.charCodeAt(b+e),!f||61==f||38==f||35==f)return b;b+=e+1}return-1}
var vc=/#|$/,wc=/[?&]($|#)/;function xc(a,b){for(var c=a.search(vc),d=0,e,f=[];0<=(e=uc(a,d,b,c));)f.push(a.substring(d,e)),d=Math.min(a.indexOf("&",e)+1||c,c);f.push(a.slice(d));return f.join("").replace(wc,"$1")}
;function yc(a){this.h=a}
;function zc(a,b,c){this.l=a;this.j=b;this.fields=c||[];this.h=new Map}
m=zc.prototype;m.Ld=function(a){var b=A.apply(1,arguments),c=this.yc(b);c?c.push(new yc(a)):this.xd(a,b)};
m.xd=function(a){var b=this.Sc(A.apply(1,arguments));this.h.set(b,[new yc(a)])};
m.yc=function(){var a=this.Sc(A.apply(0,arguments));return this.h.has(a)?this.h.get(a):void 0};
m.de=function(){var a=this.yc(A.apply(0,arguments));return a&&a.length?a[0]:void 0};
m.clear=function(){this.h.clear()};
m.Sc=function(){var a=A.apply(0,arguments);return a?a.join(","):"key"};function Ac(a,b){zc.call(this,a,3,b)}
y(Ac,zc);Ac.prototype.i=function(a){var b=A.apply(1,arguments),c=0,d=this.de(b);d&&(c=d.h);this.xd(c+a,b)};function Bc(a,b){zc.call(this,a,2,b)}
y(Bc,zc);Bc.prototype.record=function(a){this.Ld(a,A.apply(1,arguments))};function Cc(a){a&&"function"==typeof a.dispose&&a.dispose()}
;function Dc(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];Qa(d)?Dc.apply(null,d):Cc(d)}}
;function G(){this.V=this.V;this.v=this.v}
G.prototype.V=!1;G.prototype.dispose=function(){this.V||(this.V=!0,this.U())};
function Ec(a,b){a.addOnDisposeCallback(Ya(Cc,b))}
G.prototype.addOnDisposeCallback=function(a,b){this.V?void 0!==b?a.call(b):a():(this.v||(this.v=[]),this.v.push(void 0!==b?Xa(a,b):a))};
G.prototype.U=function(){if(this.v)for(;this.v.length;)this.v.shift()()};function Fc(a,b){this.type=a;this.h=this.target=b;this.defaultPrevented=this.j=!1}
Fc.prototype.stopPropagation=function(){this.j=!0};
Fc.prototype.preventDefault=function(){this.defaultPrevented=!0};var Gc=function(){if(!B.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});
try{var c=function(){};
B.addEventListener("test",c,b);B.removeEventListener("test",c,b)}catch(d){}return a}();var Hc=Oa(610401301),Ic=Oa(188588736);function Jc(){var a=B.navigator;return a&&(a=a.userAgent)?a:""}
var Kc,Lc=B.navigator;Kc=Lc?Lc.userAgentData||null:null;function Mc(a){return Hc?Kc?Kc.brands.some(function(b){return(b=b.brand)&&-1!=b.indexOf(a)}):!1:!1}
function H(a){return-1!=Jc().indexOf(a)}
;function Nc(){return Hc?!!Kc&&0<Kc.brands.length:!1}
function Oc(){return Nc()?!1:H("Opera")}
function Pc(){return H("Firefox")||H("FxiOS")}
function Qc(){return Nc()?Mc("Chromium"):(H("Chrome")||H("CriOS"))&&!(Nc()?0:H("Edge"))||H("Silk")}
;function Rc(){return Hc?!!Kc&&!!Kc.platform:!1}
function Sc(){return H("iPhone")&&!H("iPod")&&!H("iPad")}
;function Tc(a){Tc[" "](a);return a}
Tc[" "]=function(){};var Uc=Oc(),Vc=Nc()?!1:H("Trident")||H("MSIE"),Wc=H("Edge"),Xc=H("Gecko")&&!(-1!=Jc().toLowerCase().indexOf("webkit")&&!H("Edge"))&&!(H("Trident")||H("MSIE"))&&!H("Edge"),Yc=-1!=Jc().toLowerCase().indexOf("webkit")&&!H("Edge");Yc&&H("Mobile");Rc()||H("Macintosh");Rc()||H("Windows");(Rc()?"Linux"===Kc.platform:H("Linux"))||Rc()||H("CrOS");var Zc=Rc()?"Android"===Kc.platform:H("Android");Sc();H("iPad");H("iPod");Sc()||H("iPad")||H("iPod");Jc().toLowerCase().indexOf("kaios");function $c(a,b){Fc.call(this,a?a.type:"");this.relatedTarget=this.h=this.target=null;this.button=this.screenY=this.screenX=this.clientY=this.clientX=0;this.key="";this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.state=null;this.pointerId=0;this.pointerType="";this.i=null;a&&this.init(a,b)}
$a($c,Fc);var ad={2:"touch",3:"pen",4:"mouse"};
$c.prototype.init=function(a,b){var c=this.type=a.type,d=a.changedTouches&&a.changedTouches.length?a.changedTouches[0]:null;this.target=a.target||a.srcElement;this.h=b;if(b=a.relatedTarget){if(Xc){a:{try{Tc(b.nodeName);var e=!0;break a}catch(f){}e=!1}e||(b=null)}}else"mouseover"==c?b=a.fromElement:"mouseout"==c&&(b=a.toElement);this.relatedTarget=b;d?(this.clientX=void 0!==d.clientX?d.clientX:d.pageX,this.clientY=void 0!==d.clientY?d.clientY:d.pageY,this.screenX=d.screenX||0,this.screenY=d.screenY||
0):(this.clientX=void 0!==a.clientX?a.clientX:a.pageX,this.clientY=void 0!==a.clientY?a.clientY:a.pageY,this.screenX=a.screenX||0,this.screenY=a.screenY||0);this.button=a.button;this.keyCode=a.keyCode||0;this.key=a.key||"";this.charCode=a.charCode||("keypress"==c?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.pointerId=a.pointerId||0;this.pointerType="string"===typeof a.pointerType?a.pointerType:ad[a.pointerType]||"";this.state=a.state;
this.i=a;a.defaultPrevented&&$c.Ba.preventDefault.call(this)};
$c.prototype.stopPropagation=function(){$c.Ba.stopPropagation.call(this);this.i.stopPropagation?this.i.stopPropagation():this.i.cancelBubble=!0};
$c.prototype.preventDefault=function(){$c.Ba.preventDefault.call(this);var a=this.i;a.preventDefault?a.preventDefault():a.returnValue=!1};var bd="closure_listenable_"+(1E6*Math.random()|0);var cd=0;function dd(a,b,c,d,e){this.listener=a;this.proxy=null;this.src=b;this.type=c;this.capture=!!d;this.hc=e;this.key=++cd;this.Qb=this.Zb=!1}
function ed(a){a.Qb=!0;a.listener=null;a.proxy=null;a.src=null;a.hc=null}
;function fd(a){this.src=a;this.listeners={};this.h=0}
fd.prototype.add=function(a,b,c,d,e){var f=a.toString();a=this.listeners[f];a||(a=this.listeners[f]=[],this.h++);var g=gd(a,b,d,e);-1<g?(b=a[g],c||(b.Zb=!1)):(b=new dd(b,this.src,f,!!d,e),b.Zb=c,a.push(b));return b};
fd.prototype.remove=function(a,b,c,d){a=a.toString();if(!(a in this.listeners))return!1;var e=this.listeners[a];b=gd(e,b,c,d);return-1<b?(ed(e[b]),Array.prototype.splice.call(e,b,1),0==e.length&&(delete this.listeners[a],this.h--),!0):!1};
function hd(a,b){var c=b.type;c in a.listeners&&Ib(a.listeners[c],b)&&(ed(b),0==a.listeners[c].length&&(delete a.listeners[c],a.h--))}
function gd(a,b,c,d){for(var e=0;e<a.length;++e){var f=a[e];if(!f.Qb&&f.listener==b&&f.capture==!!c&&f.hc==d)return e}return-1}
;var id="closure_lm_"+(1E6*Math.random()|0),jd={},kd=0;function ld(a,b,c,d,e){if(d&&d.once)md(a,b,c,d,e);else if(Array.isArray(b))for(var f=0;f<b.length;f++)ld(a,b[f],c,d,e);else c=nd(c),a&&a[bd]?a.listen(b,c,Ra(d)?!!d.capture:!!d,e):od(a,b,c,!1,d,e)}
function od(a,b,c,d,e,f){if(!b)throw Error("Invalid event type");var g=Ra(e)?!!e.capture:!!e,h=pd(a);h||(a[id]=h=new fd(a));c=h.add(b,c,d,g,f);if(!c.proxy){d=qd();c.proxy=d;d.src=a;d.listener=c;if(a.addEventListener)Gc||(e=g),void 0===e&&(e=!1),a.addEventListener(b.toString(),d,e);else if(a.attachEvent)a.attachEvent(rd(b.toString()),d);else if(a.addListener&&a.removeListener)a.addListener(d);else throw Error("addEventListener and attachEvent are unavailable.");kd++}}
function qd(){function a(c){return b.call(a.src,a.listener,c)}
var b=sd;return a}
function md(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)md(a,b[f],c,d,e);else c=nd(c),a&&a[bd]?a.h.add(String(b),c,!0,Ra(d)?!!d.capture:!!d,e):od(a,b,c,!0,d,e)}
function td(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)td(a,b[f],c,d,e);else(d=Ra(d)?!!d.capture:!!d,c=nd(c),a&&a[bd])?a.h.remove(String(b),c,d,e):a&&(a=pd(a))&&(b=a.listeners[b.toString()],a=-1,b&&(a=gd(b,c,d,e)),(c=-1<a?b[a]:null)&&ud(c))}
function ud(a){if("number"!==typeof a&&a&&!a.Qb){var b=a.src;if(b&&b[bd])hd(b.h,a);else{var c=a.type,d=a.proxy;b.removeEventListener?b.removeEventListener(c,d,a.capture):b.detachEvent?b.detachEvent(rd(c),d):b.addListener&&b.removeListener&&b.removeListener(d);kd--;(c=pd(b))?(hd(c,a),0==c.h&&(c.src=null,b[id]=null)):ed(a)}}}
function rd(a){return a in jd?jd[a]:jd[a]="on"+a}
function sd(a,b){if(a.Qb)a=!0;else{b=new $c(b,this);var c=a.listener,d=a.hc||a.src;a.Zb&&ud(a);a=c.call(d,b)}return a}
function pd(a){a=a[id];return a instanceof fd?a:null}
var vd="__closure_events_fn_"+(1E9*Math.random()>>>0);function nd(a){if("function"===typeof a)return a;a[vd]||(a[vd]=function(b){return a.handleEvent(b)});
return a[vd]}
;function wd(){G.call(this);this.h=new fd(this);this.Za=this;this.ga=null}
$a(wd,G);wd.prototype[bd]=!0;m=wd.prototype;m.addEventListener=function(a,b,c,d){ld(this,a,b,c,d)};
m.removeEventListener=function(a,b,c,d){td(this,a,b,c,d)};
function xd(a,b){var c=a.ga;if(c){var d=[];for(var e=1;c;c=c.ga)d.push(c),++e}a=a.Za;c=b.type||b;"string"===typeof b?b=new Fc(b,a):b instanceof Fc?b.target=b.target||a:(e=b,b=new Fc(c,a),Ub(b,e));e=!0;if(d)for(var f=d.length-1;!b.j&&0<=f;f--){var g=b.h=d[f];e=yd(g,c,!0,b)&&e}b.j||(g=b.h=a,e=yd(g,c,!0,b)&&e,b.j||(e=yd(g,c,!1,b)&&e));if(d)for(f=0;!b.j&&f<d.length;f++)g=b.h=d[f],e=yd(g,c,!1,b)&&e}
m.U=function(){wd.Ba.U.call(this);this.removeAllListeners();this.ga=null};
m.listen=function(a,b,c,d){return this.h.add(String(a),b,!1,c,d)};
m.removeAllListeners=function(a){if(this.h){var b=this.h;a=a&&a.toString();var c=0,d;for(d in b.listeners)if(!a||d==a){for(var e=b.listeners[d],f=0;f<e.length;f++)++c,ed(e[f]);delete b.listeners[d];b.h--}b=c}else b=0;return b};
function yd(a,b,c,d){b=a.h.listeners[String(b)];if(!b)return!0;b=b.concat();for(var e=!0,f=0;f<b.length;++f){var g=b[f];if(g&&!g.Qb&&g.capture==c){var h=g.listener,k=g.hc||g.src;g.Zb&&hd(a.h,g);e=!1!==h.call(k,d)&&e}}return e&&!d.defaultPrevented}
;function zd(a,b){this.j=a;this.l=b;this.i=0;this.h=null}
zd.prototype.get=function(){if(0<this.i){this.i--;var a=this.h;this.h=a.next;a.next=null}else a=this.j();return a};
function Ad(a,b){a.l(b);100>a.i&&(a.i++,b.next=a.h,a.h=b)}
;function Bd(){}
function Cd(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;"ARTICLE SECTION NAV ASIDE H1 H2 H3 H4 H5 H6 HEADER FOOTER ADDRESS P HR PRE BLOCKQUOTE OL UL LH LI DL DT DD FIGURE FIGCAPTION MAIN DIV EM STRONG SMALL S CITE Q DFN ABBR RUBY RB RT RTC RP DATA TIME CODE VAR SAMP KBD SUB SUP I B U MARK BDI BDO SPAN BR WBR INS DEL PICTURE PARAM TRACK MAP TABLE CAPTION COLGROUP COL TBODY THEAD TFOOT TR TD TH SELECT DATALIST OPTGROUP OPTION OUTPUT PROGRESS METER FIELDSET LEGEND DETAILS SUMMARY MENU DIALOG SLOT CANVAS FONT CENTER ACRONYM BASEFONT BIG DIR HGROUP STRIKE TT".split(" ").concat(["BUTTON",
"INPUT"]);function Dd(a,b){this.x=void 0!==a?a:0;this.y=void 0!==b?b:0}
m=Dd.prototype;m.clone=function(){return new Dd(this.x,this.y)};
m.equals=function(a){return a instanceof Dd&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
m.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
m.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
m.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};
m.scale=function(a,b){this.x*=a;this.y*="number"===typeof b?b:a;return this};function Ed(a,b){this.width=a;this.height=b}
m=Ed.prototype;m.clone=function(){return new Ed(this.width,this.height)};
m.aspectRatio=function(){return this.width/this.height};
m.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
m.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
m.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};
m.scale=function(a,b){this.width*=a;this.height*="number"===typeof b?b:a;return this};function Fd(a){var b=document;return"string"===typeof a?b.getElementById(a):a}
function Gd(a){var b=document;a=String(a);"application/xhtml+xml"===b.contentType&&(a=a.toLowerCase());return b.createElement(a)}
function Hd(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;var Id;function Jd(){var a=B.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!H("Presto")&&(a=function(){var e=Gd("IFRAME");e.style.display="none";document.documentElement.appendChild(e);var f=e.contentWindow;e=f.document;e.open();e.close();var g="callImmediate"+Math.random(),h="file:"==f.location.protocol?"*":f.location.protocol+"//"+f.location.host;e=Xa(function(k){if(("*"==h||k.origin==h)&&k.data==g)this.port1.onmessage()},this);
f.addEventListener("message",e,!1);this.port1={};this.port2={postMessage:function(){f.postMessage(g,h)}}});
if("undefined"!==typeof a){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var e=c.Wc;c.Wc=null;e()}};
return function(e){d.next={Wc:e};d=d.next;b.port2.postMessage(0)}}return function(e){B.setTimeout(e,0)}}
;function Kd(a){B.setTimeout(function(){throw a;},0)}
;function Ld(){this.i=this.h=null}
Ld.prototype.add=function(a,b){var c=Md.get();c.set(a,b);this.i?this.i.next=c:this.h=c;this.i=c};
Ld.prototype.remove=function(){var a=null;this.h&&(a=this.h,this.h=this.h.next,this.h||(this.i=null),a.next=null);return a};
var Md=new zd(function(){return new Nd},function(a){return a.reset()});
function Nd(){this.next=this.scope=this.h=null}
Nd.prototype.set=function(a,b){this.h=a;this.scope=b;this.next=null};
Nd.prototype.reset=function(){this.next=this.scope=this.h=null};var Od,Pd=!1,Qd=new Ld;function Rd(a,b){Od||Sd();Pd||(Od(),Pd=!0);Qd.add(a,b)}
function Sd(){if(B.Promise&&B.Promise.resolve){var a=B.Promise.resolve(void 0);Od=function(){a.then(Td)}}else Od=function(){var b=Td;
"function"!==typeof B.setImmediate||B.Window&&B.Window.prototype&&B.Window.prototype.setImmediate==B.setImmediate?(Id||(Id=Jd()),Id(b)):B.setImmediate(b)}}
function Td(){for(var a;a=Qd.remove();){try{a.h.call(a.scope)}catch(b){Kd(b)}Ad(Md,a)}Pd=!1}
;function Ud(a){this.h=0;this.A=void 0;this.l=this.i=this.j=null;this.v=this.m=!1;if(a!=Bd)try{var b=this;a.call(void 0,function(c){Vd(b,2,c)},function(c){Vd(b,3,c)})}catch(c){Vd(this,3,c)}}
function Wd(){this.next=this.context=this.h=this.i=this.child=null;this.j=!1}
Wd.prototype.reset=function(){this.context=this.h=this.i=this.child=null;this.j=!1};
var Xd=new zd(function(){return new Wd},function(a){a.reset()});
function Yd(a,b,c){var d=Xd.get();d.i=a;d.h=b;d.context=c;return d}
function Zd(a){return new Ud(function(b,c){c(a)})}
Ud.prototype.then=function(a,b,c){return $d(this,"function"===typeof a?a:null,"function"===typeof b?b:null,c)};
Ud.prototype.$goog_Thenable=!0;m=Ud.prototype;m.qc=function(a,b){return $d(this,null,a,b)};
m.catch=Ud.prototype.qc;m.cancel=function(a){if(0==this.h){var b=new ae(a);Rd(function(){be(this,b)},this)}};
function be(a,b){if(0==a.h)if(a.j){var c=a.j;if(c.i){for(var d=0,e=null,f=null,g=c.i;g&&(g.j||(d++,g.child==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.h&&1==d?be(c,b):(f?(d=f,d.next==c.l&&(c.l=d),d.next=d.next.next):ce(c),de(c,e,3,b)))}a.j=null}else Vd(a,3,b)}
function ee(a,b){a.i||2!=a.h&&3!=a.h||fe(a);a.l?a.l.next=b:a.i=b;a.l=b}
function $d(a,b,c,d){var e=Yd(null,null,null);e.child=new Ud(function(f,g){e.i=b?function(h){try{var k=b.call(d,h);f(k)}catch(l){g(l)}}:f;
e.h=c?function(h){try{var k=c.call(d,h);void 0===k&&h instanceof ae?g(h):f(k)}catch(l){g(l)}}:g});
e.child.j=a;ee(a,e);return e.child}
m.jf=function(a){this.h=0;Vd(this,2,a)};
m.kf=function(a){this.h=0;Vd(this,3,a)};
function Vd(a,b,c){if(0==a.h){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.h=1;a:{var d=c,e=a.jf,f=a.kf;if(d instanceof Ud){ee(d,Yd(e||Bd,f||null,a));var g=!0}else{if(d)try{var h=!!d.$goog_Thenable}catch(l){h=!1}else h=!1;if(h)d.then(e,f,a),g=!0;else{if(Ra(d))try{var k=d.then;if("function"===typeof k){ge(d,k,e,f,a);g=!0;break a}}catch(l){f.call(a,l);g=!0;break a}g=!1}}}g||(a.A=c,a.h=b,a.j=null,fe(a),3!=b||c instanceof ae||he(a,c))}}
function ge(a,b,c,d,e){function f(k){h||(h=!0,d.call(e,k))}
function g(k){h||(h=!0,c.call(e,k))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function fe(a){a.m||(a.m=!0,Rd(a.Xd,a))}
function ce(a){var b=null;a.i&&(b=a.i,a.i=b.next,b.next=null);a.i||(a.l=null);return b}
m.Xd=function(){for(var a;a=ce(this);)de(this,a,this.h,this.A);this.m=!1};
function de(a,b,c,d){if(3==c&&b.h&&!b.j)for(;a&&a.v;a=a.j)a.v=!1;if(b.child)b.child.j=null,ie(b,c,d);else try{b.j?b.i.call(b.context):ie(b,c,d)}catch(e){je.call(null,e)}Ad(Xd,b)}
function ie(a,b,c){2==b?a.i.call(a.context,c):a.h&&a.h.call(a.context,c)}
function he(a,b){a.v=!0;Rd(function(){a.v&&je.call(null,b)})}
var je=Kd;function ae(a){bb.call(this,a)}
$a(ae,bb);ae.prototype.name="cancel";function ke(a,b){wd.call(this);this.j=a||1;this.i=b||B;this.l=Xa(this.ff,this);this.m=Za()}
$a(ke,wd);m=ke.prototype;m.enabled=!1;m.Fa=null;m.setInterval=function(a){this.j=a;this.Fa&&this.enabled?(this.stop(),this.start()):this.Fa&&this.stop()};
m.ff=function(){if(this.enabled){var a=Za()-this.m;0<a&&a<.8*this.j?this.Fa=this.i.setTimeout(this.l,this.j-a):(this.Fa&&(this.i.clearTimeout(this.Fa),this.Fa=null),xd(this,"tick"),this.enabled&&(this.stop(),this.start()))}};
m.start=function(){this.enabled=!0;this.Fa||(this.Fa=this.i.setTimeout(this.l,this.j),this.m=Za())};
m.stop=function(){this.enabled=!1;this.Fa&&(this.i.clearTimeout(this.Fa),this.Fa=null)};
m.U=function(){ke.Ba.U.call(this);this.stop();delete this.i};
function le(a,b,c){if("function"===typeof a)c&&(a=Xa(a,c));else if(a&&"function"==typeof a.handleEvent)a=Xa(a.handleEvent,a);else throw Error("Invalid listener argument");return 2147483647<Number(b)?-1:B.setTimeout(a,b||0)}
;function me(a){G.call(this);this.F=a;this.j=0;this.l=100;this.m=!1;this.i=new Map;this.A=new Set;this.flushInterval=3E4;this.h=new ke(this.flushInterval);this.h.listen("tick",this.Aa,!1,this);Ec(this,this.h)}
y(me,G);m=me.prototype;m.sendIsolatedPayload=function(a){this.m=a;this.l=1};
function ne(a){a.h.enabled||a.h.start();a.j++;a.j>=a.l&&a.Aa()}
m.Aa=function(){var a=this.i.values();a=[].concat(la(a)).filter(function(b){return b.h.size});
a.length&&this.F.flush(a,this.m);oe(a);this.j=0;this.h.enabled&&this.h.stop()};
m.Ra=function(a){var b=A.apply(1,arguments);this.i.has(a)||this.i.set(a,new Ac(a,b))};
m.Eb=function(a){var b=A.apply(1,arguments);this.i.has(a)||this.i.set(a,new Bc(a,b))};
function pe(a,b){return a.A.has(b)?void 0:a.i.get(b)}
m.Ab=function(a){this.Jd(a,1,A.apply(1,arguments))};
m.Jd=function(a,b){var c=A.apply(2,arguments),d=pe(this,a);d&&d instanceof Ac&&(d.i(b,c),ne(this))};
m.record=function(a,b){var c=A.apply(2,arguments),d=pe(this,a);d&&d instanceof Bc&&(d.record(b,c),ne(this))};
function oe(a){for(var b=0;b<a.length;b++)a[b].clear()}
;function qe(a){this.h=a;this.h.Ra("/client_streamz/bg/fic",{S:3,R:"ke"})}
function re(a){this.h=a;this.h.Ra("/client_streamz/bg/fiec",{S:3,R:"rk"},{S:3,R:"ke"},{S:2,R:"ec"})}
function se(a){this.h=a;this.h.Eb("/client_streamz/bg/fil",{S:3,R:"rk"},{S:3,R:"ke"})}
se.prototype.record=function(a,b,c){this.h.record("/client_streamz/bg/fil",a,b,c)};
function te(a){this.h=a;this.h.Ra("/client_streamz/bg/fcc",{S:2,R:"ph"},{S:3,R:"ke"})}
function ue(a){this.h=a;this.h.Eb("/client_streamz/bg/fcd",{S:2,R:"ph"},{S:3,R:"ke"})}
ue.prototype.record=function(a,b,c){this.h.record("/client_streamz/bg/fcd",a,b,c)};
function ve(a){this.h=a;this.h.Ra("/client_streamz/bg/fsc",{S:3,R:"rk"},{S:3,R:"ke"})}
function we(a){this.h=a;this.h.Eb("/client_streamz/bg/fsl",{S:3,R:"rk"},{S:3,R:"ke"})}
we.prototype.record=function(a,b,c){this.h.record("/client_streamz/bg/fsl",a,b,c)};
function xe(a){this.h=a;this.h.Eb("/client_streamz/bg/wrl",{S:3,R:"mn"},{S:2,R:"ac"},{S:2,R:"sc"},{S:3,R:"rk"})}
xe.prototype.record=function(a,b,c,d,e){this.h.record("/client_streamz/bg/wrl",a,b,c,d,e)};
function ye(a){this.h=a;this.h.Eb("/client_streamz/bg/el",{S:3,R:"en"},{S:3,R:"rk"})}
ye.prototype.record=function(a,b,c){this.h.record("/client_streamz/bg/el",a,b,c)};
function ze(a){this.h=a;this.h.Ra("/client_streamz/bg/cec",{S:2,R:"ec"},{S:3,R:"rk"})}
function Ae(a){this.h=a;this.h.Ra("/client_streamz/bg/po/csc",{S:2,R:"cs"},{S:3,R:"rk"})}
function Be(a){this.h=a;this.h.Ra("/client_streamz/bg/po/ctav",{S:3,R:"av"},{S:3,R:"rk"})}
function Ce(a){this.h=a;this.h.Ra("/client_streamz/bg/po/cwsc",{S:3,R:"su"},{S:3,R:"rk"})}
;Pc();var De=Sc()||H("iPod"),Ee=H("iPad");!H("Android")||Qc()||Pc()||Oc()||H("Silk");Qc();var Fe=H("Safari")&&!(Qc()||(Nc()?0:H("Coast"))||Oc()||(Nc()?0:H("Edge"))||(Nc()?Mc("Microsoft Edge"):H("Edg/"))||(Nc()?Mc("Opera"):H("OPR"))||Pc()||H("Silk")||H("Android"))&&!(Sc()||H("iPad")||H("iPod"));var Ge={},He=null;function Ie(a,b){Qa(a);void 0===b&&(b=0);Je();b=Ge[b];for(var c=Array(Math.floor(a.length/3)),d=b[64]||"",e=0,f=0;e<a.length-2;e+=3){var g=a[e],h=a[e+1],k=a[e+2],l=b[g>>2];g=b[(g&3)<<4|h>>4];h=b[(h&15)<<2|k>>6];k=b[k&63];c[f++]=""+l+g+h+k}l=0;k=d;switch(a.length-e){case 2:l=a[e+1],k=b[(l&15)<<2]||d;case 1:a=a[e],c[f]=""+b[a>>2]+b[(a&3)<<4|l>>4]+k+d}return c.join("")}
function Ke(a){var b=a.length,c=3*b/4;c%3?c=Math.floor(c):-1!="=.".indexOf(a[b-1])&&(c=-1!="=.".indexOf(a[b-2])?c-2:c-1);var d=new Uint8Array(c),e=0;Le(a,function(f){d[e++]=f});
return e!==c?d.subarray(0,e):d}
function Le(a,b){function c(k){for(;d<a.length;){var l=a.charAt(d++),n=He[l];if(null!=n)return n;if(!/^[\s\xa0]*$/.test(l))throw Error("Unknown base64 encoding at char: "+l);}return k}
Je();for(var d=0;;){var e=c(-1),f=c(0),g=c(64),h=c(64);if(64===h&&-1===e)break;b(e<<2|f>>4);64!=g&&(b(f<<4&240|g>>2),64!=h&&b(g<<6&192|h))}}
function Je(){if(!He){He={};for(var a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),b=["+/=","+/","-_=","-_.","-_"],c=0;5>c;c++){var d=a.concat(b[c].split(""));Ge[c]=d;for(var e=0;e<d.length;e++){var f=d[e];void 0===He[f]&&(He[f]=e)}}}}
;var Me="undefined"!==typeof Uint8Array,Ne=!Vc&&"function"===typeof btoa;function Oe(a){if(!Ne)return Ie(a);for(var b="",c=0,d=a.length-10240;c<d;)b+=String.fromCharCode.apply(null,a.subarray(c,c+=10240));b+=String.fromCharCode.apply(null,c?a.subarray(c):a);return btoa(b)}
var Pe=/[-_.]/g,Qe={"-":"+",_:"/",".":"="};function Re(a){return Qe[a]||""}
function Se(a){return Me&&null!=a&&a instanceof Uint8Array}
var Te={};var Ue;function Ve(a){if(a!==Te)throw Error("illegal external caller");}
function We(a,b){Ve(b);this.h=a;if(null!=a&&0===a.length)throw Error("ByteString should be constructed with non-empty values");}
We.prototype.sizeBytes=function(){Ve(Te);var a=this.h;if(null!=a&&!Se(a))if("string"===typeof a)if(Ne){Pe.test(a)&&(a=a.replace(Pe,Re));a=atob(a);for(var b=new Uint8Array(a.length),c=0;c<a.length;c++)b[c]=a.charCodeAt(c);a=b}else a=Ke(a);else Pa(a),a=null;return(a=null==a?a:this.h=a)?a.length:0};function Xe(){return"function"===typeof BigInt}
;var Ye=0,Ze=0;function $e(a){var b=0>a;a=Math.abs(a);var c=a>>>0;a=Math.floor((a-c)/4294967296);b&&(c=x(af(c,a)),b=c.next().value,a=c.next().value,c=b);Ye=c>>>0;Ze=a>>>0}
function bf(a,b){b>>>=0;a>>>=0;if(2097151>=b)var c=""+(4294967296*b+a);else Xe()?c=""+(BigInt(b)<<BigInt(32)|BigInt(a)):(c=(a>>>24|b<<8)&16777215,b=b>>16&65535,a=(a&16777215)+6777216*c+6710656*b,c+=8147497*b,b*=2,1E7<=a&&(c+=Math.floor(a/1E7),a%=1E7),1E7<=c&&(b+=Math.floor(c/1E7),c%=1E7),c=b+cf(c)+cf(a));return c}
function cf(a){a=String(a);return"0000000".slice(a.length)+a}
function df(){var a=Ye,b=Ze;b&2147483648?Xe()?a=""+(BigInt(b|0)<<BigInt(32)|BigInt(a>>>0)):(b=x(af(a,b)),a=b.next().value,b=b.next().value,a="-"+bf(a,b)):a=bf(a,b);return a}
function af(a,b){b=~b;a?a=~a+1:b+=1;return[a,b]}
;function ef(a){return Array.prototype.slice.call(a)}
;function ff(a){return"function"===typeof Symbol&&"symbol"===typeof Symbol()?Symbol():a}
var gf=ff(),hf=ff("0di"),jf=ff("2ex");Math.max.apply(Math,la(Object.values({vg:1,tg:2,sg:4,yg:8,xg:16,wg:32,Af:64,Ag:128,rg:256,qg:512,ug:1024,Ff:2048,zg:4096,Gf:8192})));var kf=gf?function(a,b){a[gf]|=b}:function(a,b){void 0!==a.Ua?a.Ua|=b:Object.defineProperties(a,{Ua:{value:b,
configurable:!0,writable:!0,enumerable:!1}})};
function lf(a,b,c){return c?a|b:a&~b}
var mf=gf?function(a){return a[gf]|0}:function(a){return a.Ua|0},nf=gf?function(a){return a[gf]}:function(a){return a.Ua},of=gf?function(a,b){a[gf]=b;
return a}:function(a,b){void 0!==a.Ua?a.Ua=b:Object.defineProperties(a,{Ua:{value:b,
configurable:!0,writable:!0,enumerable:!1}});return a};
function pf(a){kf(a,34);return a}
function qf(a,b){of(b,(a|0)&-14591)}
function rf(a,b){of(b,(a|34)&-14557)}
function sf(a){a=a>>14&1023;return 0===a?536870912:a}
;var tf={},uf={};function vf(a){return!(!a||"object"!==typeof a||a.se!==uf)}
function wf(a){return null!==a&&"object"===typeof a&&!Array.isArray(a)&&a.constructor===Object}
var xf;function yf(a,b,c){if(!Array.isArray(a)||a.length)return!1;var d=mf(a);if(d&1)return!0;if(!(b&&(Array.isArray(b)?b.includes(c):b.has(c))))return!1;of(a,d|1);return!0}
var zf,Af=[];of(Af,55);zf=Object.freeze(Af);function Bf(a){if(a&2)throw Error();}
function Cf(a,b,c){this.j=0;this.h=a;this.i=b;this.thisArg=c}
Cf.prototype.next=function(){if(this.j<this.h.length){var a=this.h[this.j++];return{done:!1,value:this.i?this.i.call(this.thisArg,a):a}}return{done:!0,value:void 0}};
Cf.prototype[Symbol.iterator]=function(){return new Cf(this.h,this.i,this.thisArg)};
function Df(){}
Object.freeze(new function(){});
Object.freeze(new Df);var Ef=Object.freeze(new Df);var Ff;function Gf(a){a=Error(a);ec(a,"warning");return a}
;function Hf(a){return a.displayName||a.name||"unknown type name"}
function If(a){if(null!=a&&"boolean"!==typeof a)throw Error("Expected boolean but got "+Pa(a)+": "+a);return a}
var Jf=/^-?([1-9][0-9]*|0)(\.[0-9]+)?$/;function Kf(a){var b=typeof a;return"number"===b?Number.isFinite(a):"string"!==b?!1:Jf.test(a)}
function Lf(a){if("number"!==typeof a)throw Gf("int32");if(!Number.isFinite(a))throw Gf("int32");return a|0}
function Mf(a){return null==a?a:Lf(a)}
function Nf(a){if(null==a)return a;if("string"===typeof a){if(!a)return;a=+a}if("number"===typeof a)return Number.isFinite(a)?a|0:void 0}
function Of(a){if(null!=a){var b=!!b;if(!Kf(a))throw Gf("int64");a="string"===typeof a?Pf(a):b?Qf(a):Rf(a)}return a}
function Sf(a){return"-"===a[0]?20>a.length?!0:20===a.length&&-922337<Number(a.substring(0,7)):19>a.length?!0:19===a.length&&922337>Number(a.substring(0,6))}
function Rf(a){Kf(a);a=Math.trunc(a);if(!Number.isSafeInteger(a)){$e(a);var b=Ye,c=Ze;if(a=c&2147483648)b=~b+1>>>0,c=~c>>>0,0==b&&(c=c+1>>>0);b=4294967296*c+(b>>>0);a=a?-b:b}return a}
function Qf(a){Kf(a);a=Math.trunc(a);if(Number.isSafeInteger(a))a=String(a);else{var b=String(a);Sf(b)?a=b:($e(a),a=df())}return a}
function Pf(a){Kf(a);var b=Math.trunc(Number(a));if(Number.isSafeInteger(b))return String(b);b=a.indexOf(".");-1!==b&&(a=a.substring(0,b));a.indexOf(".");if(!Sf(a)){if(16>a.length)$e(Number(a));else if(Xe())a=BigInt(a),Ye=Number(a&BigInt(4294967295))>>>0,Ze=Number(a>>BigInt(32)&BigInt(4294967295));else{b=+("-"===a[0]);Ze=Ye=0;for(var c=a.length,d=0+b,e=(c-b)%6+b;e<=c;d=e,e+=6)d=Number(a.slice(d,e)),Ze*=1E6,Ye=1E6*Ye+d,4294967296<=Ye&&(Ze+=Math.trunc(Ye/4294967296),Ze>>>=0,Ye>>>=0);b&&(b=x(af(Ye,Ze)),
a=b.next().value,b=b.next().value,Ye=a,Ze=b)}a=df()}return a}
function Tf(a){if("string"!==typeof a)throw Error();return a}
function Uf(a){if(null!=a&&"string"!==typeof a)throw Error();return a}
function Vf(a,b){if(!(a instanceof b))throw Error("Expected instanceof "+Hf(b)+" but got "+(a&&Hf(a.constructor)));}
function Wf(a,b,c,d){if(null!=a&&"object"===typeof a&&a.Fc===tf)return a;if(!Array.isArray(a))return c?d&2?(a=b[hf])?b=a:(a=new b,pf(a.D),b=b[hf]=a):b=new b:b=void 0,b;var e=c=mf(a);0===e&&(e|=d&32);e|=d&2;e!==c&&of(a,e);return new b(a)}
;var Xf;function Yf(a,b){mf(b);Xf=b;a=new a(b);Xf=void 0;return a}
function I(a,b,c){null==a&&(a=Xf);Xf=void 0;if(null==a){var d=96;c?(a=[c],d|=512):a=[];b&&(d=d&-16760833|(b&1023)<<14)}else{if(!Array.isArray(a))throw Error("narr");d=mf(a);if(d&2048)throw Error("farr");if(d&64)return a;d|=64;if(c&&(d|=512,c!==a[0]))throw Error("mid");a:{c=a;var e=c.length;if(e){var f=e-1;if(wf(c[f])){d|=256;b=f-(+!!(d&512)-1);if(1024<=b)throw Error("pvtlmt");d=d&-16760833|(b&1023)<<14;break a}}if(b){b=Math.max(b,e-(+!!(d&512)-1));if(1024<b)throw Error("spvt");d=d&-16760833|(b&1023)<<
14}}}of(a,d);return a}
;var Zf=function(){try{var a=function(){return qa(Map,[],this.constructor)};
y(a,Map);Tc(new a);return!1}catch(b){return!0}}();
function $f(){this.h=new Map}
m=$f.prototype;m.get=function(a){return this.h.get(a)};
m.set=function(a,b){this.h.set(a,b);this.size=this.h.size;return this};
m.delete=function(a){a=this.h.delete(a);this.size=this.h.size;return a};
m.clear=function(){this.h.clear();this.size=this.h.size};
m.has=function(a){return this.h.has(a)};
m.entries=function(){return this.h.entries()};
m.keys=function(){return this.h.keys()};
m.values=function(){return this.h.values()};
m.forEach=function(a,b){return this.h.forEach(a,b)};
$f.prototype[Symbol.iterator]=function(){return this.entries()};
var ag=function(){function a(){return qa(Map,[],this.constructor)}
if(Zf)return Object.setPrototypeOf($f.prototype,Map.prototype),Object.defineProperties($f.prototype,{size:{value:0,configurable:!0,enumerable:!0,writable:!0}}),$f;y(a,Map);return a}();
function bg(a){return a}
function cg(a,b,c,d){c=void 0===c?bg:c;d=void 0===d?bg:d;var e=ag.call(this)||this;var f=mf(a);f|=64;of(a,f);e.Vb=f;e.sc=b;e.Kb=c;e.Pc=e.sc?dg:d;for(var g=0;g<a.length;g++){var h=a[g],k=c(h[0],!1,!0),l=h[1];b?void 0===l&&(l=null):l=d(h[1],!1,!0,void 0,void 0,f);ag.prototype.set.call(e,k,l)}return e}
y(cg,ag);function eg(a){if(a.Vb&2)throw Error("Cannot mutate an immutable Map");}
function fg(a,b){b=void 0===b?gg:b;if(0!==a.size)return hg(a,b)}
function hg(a,b){b=void 0===b?gg:b;var c=[];a=ag.prototype.entries.call(a);for(var d;!(d=a.next()).done;)d=d.value,d[0]=b(d[0]),d[1]=b(d[1]),c.push(d);return c}
m=cg.prototype;m.clear=function(){eg(this);ag.prototype.clear.call(this)};
m.delete=function(a){eg(this);return ag.prototype.delete.call(this,this.Kb(a,!0,!1))};
m.entries=function(){var a=Array.from(ag.prototype.keys.call(this));return new Cf(a,ig,this)};
m.keys=function(){return ag.prototype.keys.call(this)};
m.values=function(){var a=Array.from(ag.prototype.keys.call(this));return new Cf(a,cg.prototype.get,this)};
m.forEach=function(a,b){var c=this;ag.prototype.forEach.call(this,function(d,e){a.call(b,c.get(e),e,c)})};
m.set=function(a,b){eg(this);a=this.Kb(a,!0,!1);return null==a?this:null==b?(ag.prototype.delete.call(this,a),this):ag.prototype.set.call(this,a,this.Pc(b,!0,!0,this.sc,!1,this.Vb))};
m.has=function(a){return ag.prototype.has.call(this,this.Kb(a,!1,!1))};
m.get=function(a){a=this.Kb(a,!1,!1);var b=ag.prototype.get.call(this,a);if(void 0!==b){var c=this.sc;return c?(c=this.Pc(b,!1,!0,c,this.Fg,this.Vb),c!==b&&ag.prototype.set.call(this,a,c),c):b}};
cg.prototype[Symbol.iterator]=function(){return this.entries()};
cg.prototype.toJSON=void 0;cg.prototype.se=uf;function dg(a,b,c,d,e,f){b&&Vf(a,d);a=Wf(a,d,c,f);e&&(a=jg(a));f&2&&mf(a.D);return a}
function gg(a){return a}
function ig(a){return[a,this.get(a)]}
;function kg(a,b){return lg(b)}
function lg(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "boolean":return a?1:0;case "object":if(a)if(Array.isArray(a)){if(yf(a,void 0,0))return}else{if(Se(a))return Oe(a);if(a instanceof We){var b=a.h;return null==b?"":"string"===typeof b?b:a.h=Oe(b)}if(a instanceof cg)return fg(a)}}return a}
;function mg(a,b,c){a=ef(a);var d=a.length,e=b&256?a[d-1]:void 0;d+=e?-1:0;for(b=b&512?1:0;b<d;b++)a[b]=c(a[b]);if(e){b=a[b]={};for(var f in e)b[f]=c(e[f])}return a}
function ng(a,b,c,d,e){if(null!=a){if(Array.isArray(a))a=yf(a,void 0,0)?void 0:e&&mf(a)&2?a:og(a,b,c,void 0!==d,e);else if(wf(a)){var f={},g;for(g in a)f[g]=ng(a[g],b,c,d,e);a=f}else a=b(a,d);return a}}
function og(a,b,c,d,e){var f=d||c?mf(a):0;d=d?!!(f&32):void 0;a=ef(a);for(var g=0;g<a.length;g++)a[g]=ng(a[g],b,c,d,e);c&&c(f,a);return a}
function pg(a){return ng(a,qg,void 0,void 0,!1)}
function qg(a){return a.Fc===tf?a.toJSON():a instanceof cg?fg(a,pg):lg(a)}
;function rg(a,b,c){c=void 0===c?rf:c;if(null!=a){if(Me&&a instanceof Uint8Array)return b?a:new Uint8Array(a);if(Array.isArray(a)){var d=mf(a);d&2||(b&&(b=0===d||!!(d&32)&&!(d&64||!(d&16))),a=b?of(a,(d|34)&-12293):og(a,rg,d&4?rf:c,!0,!0));return a}a.Fc===tf?(c=a.D,d=nf(c),a=d&2?a:Yf(a.constructor,sg(c,d,!0))):a instanceof cg&&!(a.Vb&2)&&(c=pf(hg(a,rg)),a=new cg(c,a.sc,a.Kb,a.Pc));return a}}
function sg(a,b,c){var d=c||b&2?rf:qf,e=!!(b&32);a=mg(a,b,function(f){return rg(f,e,d)});
kf(a,32|(c?2:0));return a}
function jg(a){var b=a.D,c=nf(b);return c&2?Yf(a.constructor,sg(b,c,!1)):a}
;function tg(a,b){a=a.D;return ug(a,nf(a),b)}
function vg(a,b,c,d){b=d+(+!!(b&512)-1);if(!(0>b||b>=a.length||b>=c))return a[b]}
function ug(a,b,c,d){if(-1===c)return null;var e=sf(b);if(c>=e){if(b&256)return a[a.length-1][c]}else{var f=a.length;if(d&&b&256&&(d=a[f-1][c],null!=d)){if(vg(a,b,e,c)&&null!=jf){var g;a=null!=(g=Ff)?g:Ff={};g=a[jf]||0;4<=g||(a[jf]=g+1,g=Error(),ec(g,"incident"),Kd(g))}return d}return vg(a,b,e,c)}}
function J(a,b,c){var d=a.D,e=nf(d);Bf(e);wg(d,e,b,c);return a}
function wg(a,b,c,d,e){wf(d);var f=sf(b);if(c>=f||e){var g=b;if(b&256)e=a[a.length-1];else{if(null==d)return g;e=a[f+(+!!(b&512)-1)]={};g|=256}e[c]=d;c<f&&(a[c+(+!!(b&512)-1)]=void 0);g!==b&&of(a,g);return g}a[c+(+!!(b&512)-1)]=d;b&256&&(a=a[a.length-1],c in a&&delete a[c]);return b}
function xg(a){return void 0!==yg(a,zg,11,!1)}
function Ag(a){return!!(2&a)&&!!(4&a)||!!(2048&a)}
function Bg(a,b,c){var d=a.D,e=nf(d);Bf(e);if(null==b)return wg(d,e,3),a;if(!Array.isArray(b))throw Gf();var f=mf(b),g=f,h=!!(2&f)||Object.isFrozen(b),k=!h&&(void 0===Ef||!1);if(!(4&f))for(f=21,h&&(b=ef(b),g=0,f=Cg(f,e),f=Dg(f,e,!0)),h=0;h<b.length;h++)b[h]=c(b[h]);k&&(b=ef(b),g=0,f=Cg(f,e),f=Dg(f,e,!0));f!==g&&of(b,f);wg(d,e,3,b);return a}
function Eg(a,b,c,d){a=a.D;var e=nf(a);Bf(e);for(var f=e,g=0,h=0;h<c.length;h++){var k=c[h];null!=ug(a,f,k)&&(0!==g&&(f=wg(a,f,g)),g=k)}(c=g)&&c!==b&&null!=d&&(e=wg(a,e,c));wg(a,e,b,d)}
function yg(a,b,c,d){a=a.D;var e=nf(a),f=ug(a,e,c,d);b=Wf(f,b,!1,e);b!==f&&null!=b&&wg(a,e,c,b,d);return b}
function Fg(a,b,c,d){d=void 0===d?!1:d;b=yg(a,b,c,d);if(null==b)return b;a=a.D;var e=nf(a);if(!(e&2)){var f=jg(b);f!==b&&(b=f,wg(a,e,c,b,d))}return b}
function Gg(a,b,c,d){null!=d?Vf(d,b):d=void 0;return J(a,c,d)}
function Hg(a,b,c,d){var e=a.D,f=nf(e);Bf(f);if(null==d)return wg(e,f,c),a;if(!Array.isArray(d))throw Gf();for(var g=mf(d),h=g,k=!!(2&g)||!!(2048&g),l=k||Object.isFrozen(d),n=!l&&(void 0===Ef||!1),p=!0,r=!0,t=0;t<d.length;t++){var v=d[t];Vf(v,b);k||(v=!!(mf(v.D)&2),p&&(p=!v),r&&(r=v))}k||(g=lf(g,5,!0),g=lf(g,8,p),g=lf(g,16,r));if(n||l&&g!==h)d=ef(d),h=0,g=Cg(g,f),g=Dg(g,f,!0);g!==h&&of(d,g);wg(e,f,c,d);return a}
function Cg(a,b){a=lf(a,2,!!(2&b));a=lf(a,32,!0);return a=lf(a,2048,!1)}
function Dg(a,b,c){32&b&&c||(a=lf(a,32,!1));return a}
function Ig(a,b){a=tg(a,b);var c;null==a?c=a:Kf(a)?"number"===typeof a?c=Rf(a):c=Pf(a):c=void 0;return c}
function Jg(a){a=tg(a,1);var b=void 0===b?!1:b;b=null==a?a:Kf(a)?"string"===typeof a?Pf(a):b?Qf(a):Rf(a):void 0;return b}
function Kg(a){a=tg(a,1);return null==a?a:Number.isFinite(a)?a|0:void 0}
function Lg(a,b,c){return J(a,b,Uf(c))}
function Og(a,b,c){if(null!=c){if(!Number.isFinite(c))throw Gf("enum");c|=0}return J(a,b,c)}
;function L(a,b,c){this.D=I(a,b,c)}
m=L.prototype;m.toJSON=function(){if(xf)var a=Pg(this,this.D,!1);else a=og(this.D,qg,void 0,void 0,!1),a=Pg(this,a,!0);return a};
m.serialize=function(){xf=!0;try{return JSON.stringify(this.toJSON(),kg)}finally{xf=!1}};
function Qg(a,b){if(null==b||""==b)return new a;b=JSON.parse(b);if(!Array.isArray(b))throw Error("dnarr");kf(b,32);return Yf(a,b)}
m.clone=function(){var a=this.D,b=nf(a);return Yf(this.constructor,sg(a,b,!1))};
m.Fc=tf;m.toString=function(){return Pg(this,this.D,!1).toString()};
function Pg(a,b,c){var d=Ic?void 0:a.constructor.Qa;var e=nf(c?a.D:b);a=b.length;if(!a)return b;var f;if(wf(c=b[a-1])){a:{var g=c;var h={},k=!1,l;for(l in g){var n=g[l];if(Array.isArray(n)){var p=n;if(yf(n,d,+l)||vf(n)&&0===n.size)n=null;n!=p&&(k=!0)}null!=n?h[l]=n:k=!0}if(k){for(var r in h){g=h;break a}g=null}}g!=c&&(f=!0);a--}for(l=+!!(e&512)-1;0<a;a--){r=a-1;c=b[r];r-=l;if(!(null==c||yf(c,d,r)||vf(c)&&0===c.size))break;var t=!0}if(!f&&!t)return b;b=Array.prototype.slice.call(b,0,a);g&&b.push(g);
return b}
;function Rg(a){a.Lg=!0;return a}
;function Sg(a){this.D=I(a)}
y(Sg,L);Sg.Qa=[1,2,3,4];var Tg={toString:function(a){var b=[],c=0;a-=-2147483648;b[c++]="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".charAt(a%52);for(a=Math.floor(a/52);0<a;)b[c++]="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".charAt(a%62),a=Math.floor(a/62);return b.join("")}};function Ug(a){function b(){c-=d;c-=e;c^=e>>>13;d-=e;d-=c;d^=c<<8;e-=c;e-=d;e^=d>>>13;c-=d;c-=e;c^=e>>>12;d-=e;d-=c;d^=c<<16;e-=c;e-=d;e^=d>>>5;c-=d;c-=e;c^=e>>>3;d-=e;d-=c;d^=c<<10;e-=c;e-=d;e^=d>>>15}
a=Vg(a);for(var c=2654435769,d=2654435769,e=314159265,f=a.length,g=f,h=0;12<=g;g-=12,h+=12)c+=Wg(a,h),d+=Wg(a,h+4),e+=Wg(a,h+8),b();e+=f;switch(g){case 11:e+=a[h+10]<<24;case 10:e+=a[h+9]<<16;case 9:e+=a[h+8]<<8;case 8:d+=a[h+7]<<24;case 7:d+=a[h+6]<<16;case 6:d+=a[h+5]<<8;case 5:d+=a[h+4];case 4:c+=a[h+3]<<24;case 3:c+=a[h+2]<<16;case 2:c+=a[h+1]<<8;case 1:c+=a[h+0]}b();return Tg.toString(e)}
function Vg(a){for(var b=[],c=0;c<a.length;c++)b.push(a.charCodeAt(c));return b}
function Wg(a,b){return a[b+0]+(a[b+1]<<8)+(a[b+2]<<16)+(a[b+3]<<24)}
;function Xg(a){this.D=I(a)}
y(Xg,L);var Yg=[1,2,3];function Zg(a){this.D=I(a)}
y(Zg,L);var $g=[1,2,3];function ah(a){this.D=I(a)}
y(ah,L);ah.Qa=[1];function bh(a){this.D=I(a)}
y(bh,L);bh.Qa=[3,6,4];function ch(a){this.D=I(a)}
y(ch,L);ch.Qa=[1];function dh(a){if(!a)return"";if(/^about:(?:blank|srcdoc)$/.test(a))return window.origin||"";0===a.indexOf("blob:")&&(a=a.substring(5));a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));c=a.substring(0,a.indexOf("://"));if(!c)throw Error("URI is missing protocol: "+a);if("http"!==c&&"https"!==c&&"chrome-extension"!==
c&&"moz-extension"!==c&&"file"!==c&&"android-app"!==c&&"chrome-search"!==c&&"chrome-untrusted"!==c&&"chrome"!==c&&"app"!==c&&"devtools"!==c)throw Error("Invalid URI scheme in origin: "+c);a="";var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+1);b=b.substring(0,d);if("http"===c&&"80"!==e||"https"===c&&"443"!==e)a=":"+e}return c+"://"+b+a}
;function eh(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;n=l=0}
function b(p){for(var r=g,t=0;64>t;t+=4)r[t/4]=p[t]<<24|p[t+1]<<16|p[t+2]<<8|p[t+3];for(t=16;80>t;t++)p=r[t-3]^r[t-8]^r[t-14]^r[t-16],r[t]=(p<<1|p>>>31)&4294967295;p=e[0];var v=e[1],w=e[2],C=e[3],F=e[4];for(t=0;80>t;t++){if(40>t)if(20>t){var K=C^v&(w^C);var N=1518500249}else K=v^w^C,N=1859775393;else 60>t?(K=v&w|C&(v|w),N=2400959708):(K=v^w^C,N=3395469782);K=((p<<5|p>>>27)&4294967295)+K+F+N+r[t]&4294967295;F=C;C=w;w=(v<<30|v>>>2)&4294967295;v=p;p=K}e[0]=e[0]+p&4294967295;e[1]=e[1]+v&4294967295;e[2]=
e[2]+w&4294967295;e[3]=e[3]+C&4294967295;e[4]=e[4]+F&4294967295}
function c(p,r){if("string"===typeof p){p=unescape(encodeURIComponent(p));for(var t=[],v=0,w=p.length;v<w;++v)t.push(p.charCodeAt(v));p=t}r||(r=p.length);t=0;if(0==l)for(;t+64<r;)b(p.slice(t,t+64)),t+=64,n+=64;for(;t<r;)if(f[l++]=p[t++],n++,64==l)for(l=0,b(f);t+64<r;)b(p.slice(t,t+64)),t+=64,n+=64}
function d(){var p=[],r=8*n;56>l?c(h,56-l):c(h,64-(l-56));for(var t=63;56<=t;t--)f[t]=r&255,r>>>=8;b(f);for(t=r=0;5>t;t++)for(var v=24;0<=v;v-=8)p[r++]=e[t]>>v&255;return p}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var l,n;a();return{reset:a,update:c,digest:d,Td:function(){for(var p=d(),r="",t=0;t<p.length;t++)r+="0123456789ABCDEF".charAt(Math.floor(p[t]/16))+"0123456789ABCDEF".charAt(p[t]%16);return r}}}
;function fh(a,b,c){var d=String(B.location.href);return d&&a&&b?[b,gh(dh(d),a,c||null)].join(" "):null}
function gh(a,b,c){var d=[],e=[];if(1==(Array.isArray(c)?2:1))return e=[b,a],Db(d,function(h){e.push(h)}),hh(e.join(" "));
var f=[],g=[];Db(c,function(h){g.push(h.key);f.push(h.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];Db(d,function(h){e.push(h)});
a=hh(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function hh(a){var b=eh();b.update(a);return b.Td().toLowerCase()}
;var ih={};function jh(a){this.h=a||{cookie:""}}
m=jh.prototype;m.isEnabled=function(){if(!B.navigator.cookieEnabled)return!1;if(this.h.cookie)return!0;this.set("TESTCOOKIESENABLED","1",{Ob:60});if("1"!==this.get("TESTCOOKIESENABLED"))return!1;this.remove("TESTCOOKIESENABLED");return!0};
m.set=function(a,b,c){var d=!1;if("object"===typeof c){var e=c.Me;d=c.secure||!1;var f=c.domain||void 0;var g=c.path||void 0;var h=c.Ob}if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');void 0===h&&(h=-1);c=f?";domain="+f:"";g=g?";path="+g:"";d=d?";secure":"";h=0>h?"":0==h?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(Date.now()+1E3*h)).toUTCString();this.h.cookie=a+"="+b+c+g+h+d+(null!=e?";samesite="+
e:"")};
m.get=function(a,b){for(var c=a+"=",d=(this.h.cookie||"").split(";"),e=0,f;e<d.length;e++){f=db(d[e]);if(0==f.lastIndexOf(c,0))return f.slice(c.length);if(f==a)return""}return b};
m.remove=function(a,b,c){var d=void 0!==this.get(a);this.set(a,"",{Ob:0,path:b,domain:c});return d};
m.clear=function(){for(var a=(this.h.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=db(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var kh=new jh("undefined"==typeof document?null:document);function lh(a){return!!ih.FPA_SAMESITE_PHASE2_MOD||!(void 0===a||!a)}
function mh(a){a=void 0===a?!1:a;var b=B.__SAPISID||B.__APISID||B.__3PSAPISID||B.__OVERRIDE_SID;lh(a)&&(b=b||B.__1PSAPISID);if(b)return!0;if("undefined"!==typeof document){var c=new jh(document);b=c.get("SAPISID")||c.get("APISID")||c.get("__Secure-3PAPISID");lh(a)&&(b=b||c.get("__Secure-1PAPISID"))}return!!b}
function nh(a,b,c,d){(a=B[a])||"undefined"===typeof document||(a=(new jh(document)).get(b));return a?fh(a,c,d):null}
function oh(a,b){b=void 0===b?!1:b;var c=dh(String(B.location.href)),d=[];if(mh(b)){c=0==c.indexOf("https:")||0==c.indexOf("chrome-extension:")||0==c.indexOf("moz-extension:");var e=c?B.__SAPISID:B.__APISID;e||"undefined"===typeof document||(e=new jh(document),e=e.get(c?"SAPISID":"APISID")||e.get("__Secure-3PAPISID"));(e=e?fh(e,c?"SAPISIDHASH":"APISIDHASH",a):null)&&d.push(e);c&&lh(b)&&((b=nh("__1PSAPISID","__Secure-1PAPISID","SAPISID1PHASH",a))&&d.push(b),(a=nh("__3PSAPISID","__Secure-3PAPISID",
"SAPISID3PHASH",a))&&d.push(a))}return 0==d.length?null:d.join(" ")}
;function ph(a){this.D=I(a)}
y(ph,L);ph.Qa=[2];function qh(a,b){this.intervalMs=a;this.callback=b;this.enabled=!1;this.h=function(){return Za()};
this.i=this.h()}
qh.prototype.setInterval=function(a){this.intervalMs=a;this.timer&&this.enabled?(this.stop(),this.start()):this.timer&&this.stop()};
qh.prototype.start=function(){var a=this;this.enabled=!0;this.timer||(this.timer=setTimeout(function(){a.tick()},this.intervalMs),this.i=this.h())};
qh.prototype.stop=function(){this.enabled=!1;this.timer&&(clearTimeout(this.timer),this.timer=void 0)};
qh.prototype.tick=function(){var a=this;if(this.enabled){var b=Math.max(this.h()-this.i,0);b<.8*this.intervalMs?this.timer=setTimeout(function(){a.tick()},this.intervalMs-b):(this.timer&&(clearTimeout(this.timer),this.timer=void 0),this.callback(),this.enabled&&(this.stop(),this.start()))}else this.timer=void 0};function rh(a){this.D=I(a)}
y(rh,L);function sh(a){this.D=I(a)}
y(sh,L);function th(a){this.h=this.i=this.j=a}
th.prototype.reset=function(){this.h=this.i=this.j};
th.prototype.getValue=function(){return this.i};function uh(a){this.D=I(a)}
y(uh,L);uh.prototype.fc=function(){return Kg(this)};function vh(a){this.D=I(a)}
y(vh,L);function wh(a){this.D=I(a)}
y(wh,L);function xh(a,b){Hg(a,vh,1,b)}
wh.Qa=[1];function zg(a){this.D=I(a)}
y(zg,L);var yh=["platform","platformVersion","architecture","model","uaFullVersion"],zh=new wh,Ah=null;function Bh(a,b){b=void 0===b?yh:b;if(!Ah){var c;a=null==(c=a.navigator)?void 0:c.userAgentData;if(!a||"function"!==typeof a.getHighEntropyValues||a.brands&&"function"!==typeof a.brands.map)return Promise.reject(Error("UACH unavailable"));c=(a.brands||[]).map(function(e){var f=new vh;f=Lg(f,1,e.brand);return Lg(f,2,e.version)});
xh(J(zh,2,If(a.mobile)),c);Ah=a.getHighEntropyValues(b)}var d=new Set(b);return Ah.then(function(e){var f=zh.clone();d.has("platform")&&Lg(f,3,e.platform);d.has("platformVersion")&&Lg(f,4,e.platformVersion);d.has("architecture")&&Lg(f,5,e.architecture);d.has("model")&&Lg(f,6,e.model);d.has("uaFullVersion")&&Lg(f,7,e.uaFullVersion);return f}).catch(function(){return zh.clone()})}
;function Ch(a){this.D=I(a)}
y(Ch,L);function Dh(a){this.D=I(a,4)}
y(Dh,L);function Eh(a){this.D=I(a,35)}
y(Eh,L);Eh.Qa=[3,20,27];function Fh(a){this.D=I(a,19)}
y(Fh,L);Fh.prototype.Rb=function(a){return Og(this,2,a)};
Fh.Qa=[3,5];function Gh(a){this.D=I(a,8)}
y(Gh,L);var Hh=function(a){return function(b){return Qg(a,b)}}(Gh);
Gh.Qa=[5,6,7];function Ih(a){this.D=I(a)}
y(Ih,L);var Jh;Jh=new function(a,b){this.h=a;this.ctor=b;this.isRepeated=0;this.i=Fg;this.defaultValue=void 0}(175237375,Ih);function Kh(a){G.call(this);var b=this;this.componentId="";this.j=[];this.da="";this.pageId=null;this.ga=this.W=-1;this.experimentIds=null;this.K=this.m=0;this.ja=1;this.timeoutMillis=0;this.logSource=a.logSource;this.Jb=a.Jb||function(){};
this.i=new Lh(a.logSource,a.eb);this.network=a.network;this.yb=a.yb||null;this.bufferSize=1E3;this.A=a.lf||null;this.sessionIndex=a.sessionIndex||null;this.Hb=a.Hb||!1;this.logger=null;this.withCredentials=!a.Zc;this.eb=a.eb||!1;this.F="undefined"!==typeof URLSearchParams&&!!(new URL(Mh())).searchParams&&!!(new URL(Mh())).searchParams.set;var c=Og(new Ch,1,1);Nh(this.i,c);this.l=new th(1E4);a=Oh(this,a.Tc);this.h=new qh(this.l.getValue(),a);this.ba=new qh(6E5,a);this.Hb||this.ba.start();this.eb||
(document.addEventListener("visibilitychange",function(){"hidden"===document.visibilityState&&b.xc()}),document.addEventListener("pagehide",this.xc.bind(this)))}
y(Kh,G);function Oh(a,b){return a.F?b?function(){b().then(function(){a.flush()})}:function(){a.flush()}:function(){}}
m=Kh.prototype;m.U=function(){this.xc();this.h.stop();this.ba.stop();G.prototype.U.call(this)};
m.log=function(a){if(this.F){a=a.clone();var b=this.ja++;a=J(a,21,Of(b));this.componentId&&Lg(a,26,this.componentId);if(!Jg(a)){var c=Date.now();b=a;c=Number.isFinite(c)?c.toString():"0";J(b,1,Of(c))}null==Ig(a,15)&&J(a,15,Of(60*(new Date).getTimezoneOffset()));this.experimentIds&&(b=a,c=this.experimentIds.clone(),Gg(b,ph,16,c));b=this.j.length-this.bufferSize+1;0<b&&(this.j.splice(0,b),this.m+=b);this.j.push(a);this.Hb||this.h.enabled||this.h.start()}};
m.flush=function(a,b){var c=this;if(0===this.j.length)a&&a();else{var d=Date.now();if(this.ga>d&&this.W<d)b&&b("throttled");else{this.network&&("function"===typeof this.network.fc?Ph(this.i,this.network.fc()):Ph(this.i,0));var e=Qh(this.i,this.j,this.m,this.K,this.yb);d={};var f=this.Jb();f&&(d.Authorization=f);this.A||(this.A=Mh());try{var g=(new URL(this.A)).toString()}catch(k){g=(new URL(this.A,window.location.origin)).toString()}g=new URL(g);this.sessionIndex&&(d["X-Goog-AuthUser"]=this.sessionIndex,
g.searchParams.set("authuser",this.sessionIndex));this.pageId&&(Object.defineProperty(d,"X-Goog-PageId",{value:this.pageId}),g.searchParams.set("pageId",this.pageId));if(f&&this.da===f)b&&b("stale-auth-token");else{this.j=[];this.h.enabled&&this.h.stop();this.m=0;var h=e.serialize();d={url:g.toString(),body:h,Dg:1,td:d,requestType:"POST",withCredentials:this.withCredentials,timeoutMillis:this.timeoutMillis};g=function(k){c.l.reset();c.h.setInterval(c.l.getValue());if(k){var l=null;try{var n=JSON.stringify(JSON.parse(k.replace(")]}'\n",
"")));l=Hh(n)}catch(r){}if(l){k=Number;n="-1";n=void 0===n?"0":n;var p=Jg(l);k=k(null!=p?p:n);0<k&&(c.W=Date.now(),c.ga=c.W+k);l=Jh.ctor?Jh.i(l,Jh.ctor,Jh.h,!0):Jh.i(l,Jh.h,null,!0);if(k=null===l?void 0:l)l=-1,l=void 0===l?0:l,k=Nf(tg(k,1)),l=null!=k?k:l,-1!==l&&(c.l=new th(1>l?1:l),c.h.setInterval(c.l.getValue()))}}a&&a();c.K=0};
h=function(k,l){var n=e.D;var p=nf(n),r=p,t=!(2&p),v=!!(2&r);p=v?1:2;t&&(t=!v);v=ug(n,r,3);v=Array.isArray(v)?v:zf;var w=mf(v),C=!!(4&w);if(!C){var F=w;0===F&&(F=Cg(F,r));F=lf(F,1,!0);w=v;var K=r,N=!!(2&F);N&&(K=lf(K,2,!0));for(var S=!N,da=!0,ta=0,P=0;ta<w.length;ta++){var ea=Wf(w[ta],Eh,!1,K);if(ea instanceof Eh){if(!N){var na=!!(mf(ea.D)&2);S&&(S=!na);da&&(da=na)}w[P++]=ea}}P<ta&&(w.length=P);F=lf(F,4,!0);F=lf(F,16,da);F=lf(F,8,S);of(w,F);N&&Object.freeze(w);w=F}if(t&&!(8&w||!v.length&&(1===p||
4===p&&32&w))){Ag(w)&&(v=ef(v),w=Cg(w,r),r=wg(n,r,3,v));t=v;for(F=0;F<t.length;F++)K=t[F],N=jg(K),K!==N&&(t[F]=N);w=lf(w,8,!0);w=lf(w,16,!t.length);of(t,w)}Ag(w)||(t=w,(F=1===p||4===p&&!!(32&w))?(K=!!(32&w),w=lf(w,!v.length||16&w&&(!C||K)?2:2048,!0)):w=Dg(w,r,!1),w!==t&&of(v,w),F&&Object.freeze(v));2===p&&Ag(w)&&(v=ef(v),w=Cg(w,r),w=Dg(w,r,!1),of(v,w),wg(n,r,3,v));n=v;r=Ig(e,14);p=c.l;p.h=Math.min(3E5,2*p.h);p.i=Math.min(3E5,p.h+Math.round(.2*(Math.random()-.5)*p.h));c.h.setInterval(c.l.getValue());
401===k&&f&&(c.da=f);r&&(c.m+=r);void 0===l&&(l=c.isRetryable(k));l&&(c.j=n.concat(c.j),c.Hb||c.h.enabled||c.h.start());b&&b("net-send-failed",k);++c.K};
c.network&&c.network.send(d,g,h)}}}};
m.xc=function(){Rh(this.i,!0);this.flush();Rh(this.i,!1)};
m.isRetryable=function(a){return 500<=a&&600>a||401===a||0===a};
function Mh(){return"https://play.google.com/log?format=json&hasfast=true"}
function Lh(a,b){this.eb=b=void 0===b?!1:b;this.i=this.locale=null;this.h=new Fh;Number.isInteger(a)&&this.h.Rb(a);b||(this.locale=document.documentElement.getAttribute("lang"));Nh(this,new Ch)}
Lh.prototype.Rb=function(a){this.h.Rb(a);return this};
function Nh(a,b){Gg(a.h,Ch,1,b);Kg(b)||Og(b,1,1);if(!a.eb){b=Sh(a);var c=tg(b,5);(null==c||"string"===typeof c)&&c||Lg(b,5,a.locale)}a.i&&(b=Sh(a),Fg(b,wh,9)||Gg(b,wh,9,a.i))}
function Ph(a,b){xg(Th(a))&&(a=Uh(a),Og(a,1,b))}
function Rh(a,b){xg(Th(a))&&(a=Uh(a),J(a,2,If(b)))}
function Th(a){return Fg(a.h,Ch,1)}
function Vh(a){var b=void 0===b?yh:b;var c=a.eb?void 0:window;c?Bh(c,b).then(function(d){a.i=d;d=Sh(a);Gg(d,wh,9,a.i);return!0}).catch(function(){return!1}):Promise.resolve(!1)}
function Sh(a){a=Th(a);var b=Fg(a,zg,11);b||(b=new zg,Gg(a,zg,11,b));return b}
function Uh(a){a=Sh(a);var b=Fg(a,uh,10);b||(b=new uh,J(b,2,If(!1)),Gg(a,uh,10,b));return b}
function Qh(a,b,c,d,e){var f=0,g=0;c=void 0===c?0:c;f=void 0===f?0:f;g=void 0===g?0:g;d=void 0===d?0:d;if(xg(Th(a))){var h=Uh(a);J(h,3,Mf(d))}xg(Th(a))&&(d=Uh(a),J(d,4,Mf(f)));xg(Th(a))&&(f=Uh(a),J(f,5,Mf(g)));a=a.h.clone();g=Date.now().toString();a=J(a,4,Of(g));b=b.slice();b=Hg(a,Eh,3,b);e&&(a=new rh,e=J(a,13,Mf(e)),a=new sh,e=Gg(a,rh,2,e),a=new Dh,e=Gg(a,sh,1,e),e=Og(e,2,9),Gg(b,Dh,18,e));c&&J(b,14,Of(c));return b}
;function Wh(){this.Kd="undefined"!==typeof AbortController}
Wh.prototype.send=function(a,b,c){var d=this,e,f,g,h,k,l,n,p,r,t;return z(function(v){switch(v.h){case 1:return f=(e=d.Kd?new AbortController:void 0)?setTimeout(function(){e.abort()},a.timeoutMillis):void 0,Aa(v,2,3),g=Object.assign({},{method:a.requestType,
headers:Object.assign({},a.td)},a.body&&{body:a.body},a.withCredentials&&{credentials:"include"},{signal:a.timeoutMillis&&e?e.signal:null}),v.yield(fetch(a.url,g),5);case 5:h=v.i;if(200!==h.status){null==(k=c)||k(h.status);v.B(3);break}if(null==(l=b)){v.B(7);break}return v.yield(h.text(),8);case 8:l(v.i);case 7:case 3:v.K=[v.j];v.l=0;v.v=0;clearTimeout(f);Ca(v);break;case 2:n=Ba(v);switch(null==(p=n)?void 0:p.name){case "AbortError":null==(r=c)||r(408);break;default:null==(t=c)||t(400)}v.B(3)}})};
Wh.prototype.fc=function(){return 4};function Xh(a,b){G.call(this);this.logSource=a;this.sessionIndex=b;this.j="https://play.google.com/log?format=json&hasfast=true";this.h=null;this.l=!1;this.network=null;this.componentId="";this.pageId=this.i=this.yb=null}
y(Xh,G);Xh.prototype.Zc=function(){this.m=!0;return this};
function Yh(a){a.network||(a.network=new Wh);var b=new Kh({logSource:a.logSource,Jb:a.Jb?a.Jb:oh,sessionIndex:a.sessionIndex,lf:a.j,eb:a.l,Hb:!1,Zc:a.m,Tc:a.Tc,network:a.network});Ec(a,b);if(a.h){var c=a.h,d=Sh(b.i);Lg(d,7,c)}a.componentId&&(b.componentId=a.componentId);a.yb&&(b.yb=a.yb);a.pageId&&(b.pageId=a.pageId);a.i&&((d=a.i)?(b.experimentIds||(b.experimentIds=new ph),c=b.experimentIds,d=d.serialize(),Lg(c,4,d)):b.experimentIds&&J(b.experimentIds,4));Vh(b.i);a.network.Rb&&a.network.Rb(a.logSource);
a.network.Xe&&a.network.Xe(b);return b}
;function Zh(a,b,c,d,e,f,g){a=void 0===a?-1:a;b=void 0===b?"":b;c=void 0===c?"":c;d=void 0===d?!1:d;e=void 0===e?"":e;G.call(this);this.logSource=a;this.componentId=b;f?b=f:(a=new Xh(a,"0"),a.componentId=b,Ec(this,a),""!==c&&(a.j=c),d&&(a.l=!0),e&&(a.h=e),g&&(a.network=g),b=Yh(a));this.h=b}
y(Zh,G);
Zh.prototype.flush=function(a){var b=a||[];if(b.length){a=new ch;for(var c=[],d=0;d<b.length;d++){var e=b[d];var f=new bh;f=Lg(f,1,e.l);for(var g=[],h=0;h<e.fields.length;h++)g.push(e.fields[h].R);f=Bg(f,g,Tf);g=[];h=[];for(var k=x(e.h.keys()),l=k.next();!l.done;l=k.next())h.push(l.value.split(","));for(k=0;k<h.length;k++){l=h[k];var n=e.j;for(var p=e.yc(l)||[],r=[],t=0;t<p.length;t++){var v=p[t],w=v&&v.h;v=new Zg;switch(n){case 3:w=Number(w);Number.isFinite(w)&&Eg(v,1,$g,Of(w));break;case 2:w=Number(w);
if(null!=w&&"number"!==typeof w)throw Error("Value of float/double field must be a number, found "+typeof w+": "+w);Eg(v,2,$g,w)}r.push(v)}n=r;for(p=0;p<n.length;p++){r=n[p];t=new ah;r=Gg(t,Zg,2,r);t=l;v=[];w=[];for(var C=0;C<e.fields.length;C++)w.push(e.fields[C].S);for(C=0;C<w.length;C++){var F=w[C],K=t[C],N=new Xg;switch(F){case 3:Eg(N,1,Yg,Uf(String(K)));break;case 2:F=Number(K);Number.isFinite(F)&&Eg(N,2,Yg,Mf(F));break;case 1:Eg(N,3,Yg,If("true"===K))}v.push(N)}Hg(r,Xg,1,v);g.push(r)}}Hg(f,
ah,4,g);c.push(f);e.clear()}Hg(a,bh,1,c);b=this.h;b.F&&(a instanceof Eh?b.log(a):(c=new Eh,a=a.serialize(),a=Lg(c,8,a),b.log(a)));this.h.flush()}};function $h(){}
$h.prototype.serialize=function(a){var b=[];ai(this,a,b);return b.join("")};
function ai(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(Array.isArray(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),ai(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),bi(d,c),c.push(":"),ai(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":bi(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var ci={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\v":"\\u000b"},di=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function bi(a,b){b.push('"',a.replace(di,function(c){var d=ci[c];d||(d="\\u"+(c.charCodeAt(0)|65536).toString(16).slice(1),ci[c]=d);return d}),'"')}
;function ei(){}
ei.prototype.h=null;ei.prototype.getOptions=function(){var a;(a=this.h)||(a=this.h={});return a};var fi;function gi(){}
$a(gi,ei);fi=new gi;function hi(a){wd.call(this);this.headers=new Map;this.Ga=a||null;this.i=!1;this.K=this.T=null;this.l=this.da="";this.j=this.ba=this.m=this.W=!1;this.F=0;this.A=null;this.xa="";this.ja=!1}
$a(hi,wd);var ii=/^https?$/i,ji=["POST","PUT"],ki=[];function li(a,b,c,d,e,f,g){var h=new hi;ki.push(h);b&&h.listen("complete",b);h.h.add("ready",h.Rd,!0,void 0,void 0);f&&(h.F=Math.max(0,f));g&&(h.ja=g);h.send(a,c,d,e)}
m=hi.prototype;m.Rd=function(){this.dispose();Ib(ki,this)};
m.send=function(a,b,c,d){if(this.T)throw Error("[goog.net.XhrIo] Object is active with another request="+this.da+"; newUri="+a);b=b?b.toUpperCase():"GET";this.da=a;this.l="";this.W=!1;this.i=!0;this.T=new XMLHttpRequest;this.K=this.Ga?this.Ga.getOptions():fi.getOptions();this.T.onreadystatechange=Xa(this.nd,this);try{this.getStatus(),this.ba=!0,this.T.open(b,String(a),!0),this.ba=!1}catch(g){this.getStatus();mi(this,g);return}a=c||"";c=new Map(this.headers);if(d)if(Object.getPrototypeOf(d)===Object.prototype)for(var e in d)c.set(e,
d[e]);else if("function"===typeof d.keys&&"function"===typeof d.get){e=x(d.keys());for(var f=e.next();!f.done;f=e.next())f=f.value,c.set(f,d.get(f))}else throw Error("Unknown input type for opt_headers: "+String(d));d=Array.from(c.keys()).find(function(g){return"content-type"==g.toLowerCase()});
e=B.FormData&&a instanceof B.FormData;!(0<=Cb(ji,b))||d||e||c.set("Content-Type","application/x-www-form-urlencoded;charset=utf-8");b=x(c);for(d=b.next();!d.done;d=b.next())c=x(d.value),d=c.next().value,c=c.next().value,this.T.setRequestHeader(d,c);this.xa&&(this.T.responseType=this.xa);"withCredentials"in this.T&&this.T.withCredentials!==this.ja&&(this.T.withCredentials=this.ja);try{ni(this),0<this.F&&(this.getStatus(),this.A=le(this.hf,this.F,this)),this.getStatus(),this.m=!0,this.T.send(a),this.m=
!1}catch(g){this.getStatus(),mi(this,g)}};
m.hf=function(){"undefined"!=typeof Na&&this.T&&(this.l="Timed out after "+this.F+"ms, aborting",this.getStatus(),xd(this,"timeout"),this.abort(8))};
function mi(a,b){a.i=!1;a.T&&(a.j=!0,a.T.abort(),a.j=!1);a.l=b;oi(a);pi(a)}
function oi(a){a.W||(a.W=!0,xd(a,"complete"),xd(a,"error"))}
m.abort=function(){this.T&&this.i&&(this.getStatus(),this.i=!1,this.j=!0,this.T.abort(),this.j=!1,xd(this,"complete"),xd(this,"abort"),pi(this))};
m.U=function(){this.T&&(this.i&&(this.i=!1,this.j=!0,this.T.abort(),this.j=!1),pi(this,!0));hi.Ba.U.call(this)};
m.nd=function(){this.V||(this.ba||this.m||this.j?qi(this):this.Ae())};
m.Ae=function(){qi(this)};
function qi(a){if(a.i&&"undefined"!=typeof Na)if(a.K[1]&&4==ri(a)&&2==a.getStatus())a.getStatus();else if(a.m&&4==ri(a))le(a.nd,0,a);else if(xd(a,"readystatechange"),a.isComplete()){a.getStatus();a.i=!1;try{if(si(a))xd(a,"complete"),xd(a,"success");else{try{var b=2<ri(a)?a.T.statusText:""}catch(c){b=""}a.l=b+" ["+a.getStatus()+"]";oi(a)}}finally{pi(a)}}}
function pi(a,b){if(a.T){ni(a);var c=a.T,d=a.K[0]?function(){}:null;
a.T=null;a.K=null;b||xd(a,"ready");try{c.onreadystatechange=d}catch(e){}}}
function ni(a){a.A&&(B.clearTimeout(a.A),a.A=null)}
m.isActive=function(){return!!this.T};
m.isComplete=function(){return 4==ri(this)};
function si(a){var b=a.getStatus();a:switch(b){case 200:case 201:case 202:case 204:case 206:case 304:case 1223:var c=!0;break a;default:c=!1}if(!c){if(b=0===b)a=nc(1,String(a.da)),!a&&B.self&&B.self.location&&(a=B.self.location.protocol.slice(0,-1)),b=!ii.test(a?a.toLowerCase():"");c=b}return c}
function ri(a){return a.T?a.T.readyState:0}
m.getStatus=function(){try{return 2<ri(this)?this.T.status:-1}catch(a){return-1}};
m.getLastError=function(){return"string"===typeof this.l?this.l:String(this.l)};function ti(){}
ti.prototype.send=function(a,b,c){b=void 0===b?function(){}:b;
c=void 0===c?function(){}:c;
li(a.url,function(d){d=d.target;if(si(d)){try{var e=d.T?d.T.responseText:""}catch(f){e=""}b(e)}else c(d.getStatus())},a.requestType,a.body,a.td,a.timeoutMillis,a.withCredentials)};
ti.prototype.fc=function(){return 1};function ui(a,b,c){this.logger=a;this.event=b;if(void 0===c||c)this.h=vi()}
ui.prototype.start=function(){this.h=vi()};
ui.prototype.done=function(){null!=this.h&&this.logger.Nb(this.event,vi()-this.h)};
function wi(){}
m=wi.prototype;m.Cc=function(){};
m.Nb=function(){};
m.kd=function(a){return a()};
m.Ha=function(){};
m.Aa=function(){};
function xi(a,b,c,d){G.call(this);this.Ea=b;this.i=new Map;this.j=new Map;b=new Xh(1828,"0");b.h="21";b.network=new ti;if(d){var e=new Sg;d=Bg(e,d,Lf);b.i=d}this.m=new Zh(1828,"","",!1,"",Yh(b));this.h=new me(this.m);c&&(this.h.l=1E5,c=this.h,c.flushInterval=3E4,c.h.setInterval(3E4));this.ba=new se(this.h);this.da=new ve(this.h);this.ga=new we(this.h);this.W=new re(this.h);this.A=new te(this.h);this.F=new ue(this.h);this.errorCount=new ze(this.h);this.K=new ye(this.h);new xe(this.h);new Ae(this.h);
new Be(this.h);new Ce(this.h);this.l=Ug(a);a=new qe(this.h);this.i.set("h",1);this.i.set("u",2);this.i.set("k",3);this.i.set("P",4);this.i.set("p",5);this.j.set(25,1);this.j.set(26,2);this.j.set(27,3);this.j.set(28,4);a.h.Ab("/client_streamz/bg/fic",this.Ea);Ec(this,this.m);Ec(this,this.h)}
y(xi,G);m=xi.prototype;m.Cc=function(){this.da.h.Ab("/client_streamz/bg/fsc",this.l,this.Ea)};
m.Nb=function(a,b){if("t"===a)this.ba.record(b,this.l,this.Ea);else if("n"===a)this.ga.record(b,this.l,this.Ea);else if("h"===a||"u"===a||"k"===a||"P"===a||"p"===a){if(a=this.i.get(a))this.A.h.Ab("/client_streamz/bg/fcc",a,this.Ea),this.F.record(b,a,this.Ea)}else this.K.record(b,a,this.Ea)};
m.kd=function(a,b){var c=vi();a=a();this.Nb(b,vi()-c);return a};
m.Ha=function(a){var b=this.j.get(a);b?this.W.h.Ab("/client_streamz/bg/fiec",this.l,this.Ea,b):this.errorCount.h.Ab("/client_streamz/bg/cec",a,this.Ea)};
m.Aa=function(){this.h.Aa()};
function vi(){var a,b,c;return null!=(c=null==(a=globalThis.performance)?void 0:null==(b=a.now)?void 0:b.call(a))?c:Date.now()}
;function yi(){var a=this;this.promise=new Promise(function(b,c){a.resolve=b;a.reject=c})}
;function zi(a){function b(t,v,w){Promise.resolve().then(function(){p.done();d.h&&d.ea.Aa();n.resolve({Nd:t,af:v,Rg:w})})}
function c(t,v,w,C){if(h){var F="k";v?F="h":w&&(F="u");"k"!==F?0!==C&&d.ea.Nb(F,t):0>=d.i?(d.ea.Nb(F,t),d.i=Math.floor(200*Math.random())):d.i--}}
G.call(this);var d=this;this.h=!1;this.i=Math.floor(200*Math.random());var e=a.program;var f=a.ge;var g=Math.random(),h=.3>g;null!=a.Pd&&(h=g<a.Pd);h&&(this.h=!0);var k=new G;this.addOnDisposeCallback(function(){d.j.then(function(t){t=t.af;d.ea.Aa();null==t||t();k.dispose()})});
if(!1!==a.Ge)if(a.ea)this.ea=a.ea;else{var l;Ec(k,this.ea=new xi(f,null!=(l=a.Ea)?l:"_",this.h))}else this.ea=new wi;var n=new yi;this.j=n.promise;var p=new ui(this.ea,"t",!1);if(!B[f])throw this.ea.Ha(25),this.ea.Aa(),Error("EGOU");if(!B[f].a)throw this.ea.Ha(26),this.ea.Aa(),Error("ELIU");try{var r=B[f].a;p.start();this.l=x(r(e,b,!0,a.bh,c)).next().value;this.Ze=n.promise.then(function(){})}catch(t){throw this.ea.Ha(28),this.ea.Aa(),t;
}}
y(zi,G);zi.prototype.snapshot=function(a){var b=this;if(this.V)throw Error("Already disposed");this.ea.Cc();return this.j.then(function(c){var d=c.Nd;return new Promise(function(e){var f=new ui(b.ea,"n");d(function(g){f.done();b.h&&b.ea.Aa();e(g)},[a.Yc,
a.bf,a.nf,a.cf])})})};
zi.prototype.zd=function(a){var b=this;if(this.V)throw Error("Already disposed");this.ea.Cc();var c=this.ea.kd(function(){return b.l([a.Yc,a.bf,a.nf,a.cf])},"n");
this.h&&this.ea.Aa();return c};var Ai=window;ib("csi.gstatic.com");ib("googleads.g.doubleclick.net");ib("partner.googleadservices.com");ib("pubads.g.doubleclick.net");ib("securepubads.g.doubleclick.net");ib("tpc.googlesyndication.com");function Bi(a){var b=Ci;if(b)for(var c in b)Object.prototype.hasOwnProperty.call(b,c)&&a(b[c],c,b)}
function Di(){var a=[];Bi(function(b){a.push(b)});
return a}
var Ci={pf:"allow-forms",qf:"allow-modals",rf:"allow-orientation-lock",sf:"allow-pointer-lock",tf:"allow-popups",uf:"allow-popups-to-escape-sandbox",vf:"allow-presentation",wf:"allow-same-origin",xf:"allow-scripts",yf:"allow-top-navigation",zf:"allow-top-navigation-by-user-activation"},Ei=Cd(function(){return Di()});
function Fi(){var a=Gi(),b={};Db(Ei(),function(c){a.sandbox&&a.sandbox.supports&&a.sandbox.supports(c)&&(b[c]=!0)});
return b}
function Gi(){var a=void 0===a?document:a;return a.createElement("iframe")}
;function Hi(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var Ii=(new Date).getTime();function Ji(){var a=Ki;return Rg(function(b){for(var c in a)if(b===a[c]&&!/^[0-9]+$/.test(c))return!0;return!1})}
;function Li(a){wd.call(this);var b=this;this.A=this.j=0;this.Da=null!=a?a:{pa:function(e,f){return setTimeout(e,f)},
qa:function(e){clearTimeout(e)}};
var c,d;this.i=null!=(d=null==(c=window.navigator)?void 0:c.onLine)?d:!0;this.l=function(){return z(function(e){return e.yield(Mi(b),0)})};
window.addEventListener("offline",this.l);window.addEventListener("online",this.l);this.A||Ni(this)}
y(Li,wd);function Oi(){var a=Pi;Li.h||(Li.h=new Li(a));return Li.h}
Li.prototype.dispose=function(){window.removeEventListener("offline",this.l);window.removeEventListener("online",this.l);this.Da.qa(this.A);delete Li.h};
Li.prototype.va=function(){return this.i};
function Ni(a){a.A=a.Da.pa(function(){var b;return z(function(c){if(1==c.h)return a.i?(null==(b=window.navigator)?0:b.onLine)?c.B(3):c.yield(Mi(a),3):c.yield(Mi(a),3);Ni(a);c.h=0})},3E4)}
function Mi(a,b){return a.m?a.m:a.m=new Promise(function(c){var d,e,f,g;return z(function(h){switch(h.h){case 1:return d=window.AbortController?new window.AbortController:void 0,f=null==(e=d)?void 0:e.signal,g=!1,Aa(h,2,3),d&&(a.j=a.Da.pa(function(){d.abort()},b||2E4)),h.yield(fetch("/generate_204",{method:"HEAD",
signal:f}),5);case 5:g=!0;case 3:h.K=[h.j];h.l=0;h.v=0;a.m=void 0;a.j&&(a.Da.qa(a.j),a.j=0);g!==a.i&&(a.i=g,a.i?xd(a,"networkstatus-online"):xd(a,"networkstatus-offline"));c(g);Ca(h);break;case 2:Ba(h),g=!1,h.B(3)}})})}
;function Qi(){this.data=[];this.h=-1}
Qi.prototype.set=function(a,b){b=void 0===b?!0:b;0<=a&&52>a&&Number.isInteger(a)&&this.data[a]!==b&&(this.data[a]=b,this.h=-1)};
Qi.prototype.get=function(a){return!!this.data[a]};
function Ri(a){-1===a.h&&(a.h=a.data.reduce(function(b,c,d){return b+(c?Math.pow(2,d):0)},0));
return a.h}
;function Si(){this.blockSize=-1}
;function Ti(){this.blockSize=-1;this.blockSize=64;this.h=[];this.v=[];this.m=[];this.j=[];this.j[0]=128;for(var a=1;a<this.blockSize;++a)this.j[a]=0;this.l=this.i=0;this.reset()}
$a(Ti,Si);Ti.prototype.reset=function(){this.h[0]=1732584193;this.h[1]=4023233417;this.h[2]=2562383102;this.h[3]=271733878;this.h[4]=3285377520;this.l=this.i=0};
function Ui(a,b,c){c||(c=0);var d=a.m;if("string"===typeof b)for(var e=0;16>e;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;16>e;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(e=16;80>e;e++){var f=d[e-3]^d[e-8]^d[e-14]^d[e-16];d[e]=(f<<1|f>>>31)&4294967295}b=a.h[0];c=a.h[1];var g=a.h[2],h=a.h[3],k=a.h[4];for(e=0;80>e;e++){if(40>e)if(20>e){f=h^c&(g^h);var l=1518500249}else f=c^g^h,l=1859775393;else 60>e?(f=c&g|h&(c|g),l=2400959708):
(f=c^g^h,l=3395469782);f=(b<<5|b>>>27)+f+k+l+d[e]&4294967295;k=h;h=g;g=(c<<30|c>>>2)&4294967295;c=b;b=f}a.h[0]=a.h[0]+b&4294967295;a.h[1]=a.h[1]+c&4294967295;a.h[2]=a.h[2]+g&4294967295;a.h[3]=a.h[3]+h&4294967295;a.h[4]=a.h[4]+k&4294967295}
Ti.prototype.update=function(a,b){if(null!=a){void 0===b&&(b=a.length);for(var c=b-this.blockSize,d=0,e=this.v,f=this.i;d<b;){if(0==f)for(;d<=c;)Ui(this,a,d),d+=this.blockSize;if("string"===typeof a)for(;d<b;){if(e[f]=a.charCodeAt(d),++f,++d,f==this.blockSize){Ui(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.blockSize){Ui(this,e);f=0;break}}this.i=f;this.l+=b}};
Ti.prototype.digest=function(){var a=[],b=8*this.l;56>this.i?this.update(this.j,56-this.i):this.update(this.j,this.blockSize-(this.i-56));for(var c=this.blockSize-1;56<=c;c--)this.v[c]=b&255,b/=256;Ui(this,this.v);for(c=b=0;5>c;c++)for(var d=24;0<=d;d-=8)a[b]=this.h[c]>>d&255,++b;return a};function Vi(a){return"string"==typeof a.className?a.className:a.getAttribute&&a.getAttribute("class")||""}
function Wi(a,b){"string"==typeof a.className?a.className=b:a.setAttribute&&a.setAttribute("class",b)}
function Xi(a,b){a.classList?b=a.classList.contains(b):(a=a.classList?a.classList:Vi(a).match(/\S+/g)||[],b=0<=Cb(a,b));return b}
function Yi(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):Xi(a,"inverted-hdpi")&&Wi(a,Array.prototype.filter.call(a.classList?a.classList:Vi(a).match(/\S+/g)||[],function(b){return"inverted-hdpi"!=b}).join(" "))}
;function Zi(){}
Zi.prototype.next=function(){return $i};
var $i={done:!0,value:void 0};Zi.prototype.mb=function(){return this};function aj(a){if(a instanceof bj||a instanceof cj||a instanceof dj)return a;if("function"==typeof a.next)return new bj(function(){return a});
if("function"==typeof a[Symbol.iterator])return new bj(function(){return a[Symbol.iterator]()});
if("function"==typeof a.mb)return new bj(function(){return a.mb()});
throw Error("Not an iterator or iterable.");}
function bj(a){this.h=a}
bj.prototype.mb=function(){return new cj(this.h())};
bj.prototype[Symbol.iterator]=function(){return new dj(this.h())};
bj.prototype.i=function(){return new dj(this.h())};
function cj(a){this.h=a}
y(cj,Zi);cj.prototype.next=function(){return this.h.next()};
cj.prototype[Symbol.iterator]=function(){return new dj(this.h)};
cj.prototype.i=function(){return new dj(this.h)};
function dj(a){bj.call(this,function(){return a});
this.j=a}
y(dj,bj);dj.prototype.next=function(){return this.j.next()};function M(a){G.call(this);this.m=1;this.j=[];this.l=0;this.h=[];this.i={};this.A=!!a}
$a(M,G);m=M.prototype;m.subscribe=function(a,b,c){var d=this.i[a];d||(d=this.i[a]=[]);var e=this.m;this.h[e]=a;this.h[e+1]=b;this.h[e+2]=c;this.m=e+3;d.push(e);return e};
m.unsubscribe=function(a,b,c){if(a=this.i[a]){var d=this.h;if(a=a.find(function(e){return d[e+1]==b&&d[e+2]==c}))return this.Bb(a)}return!1};
m.Bb=function(a){var b=this.h[a];if(b){var c=this.i[b];0!=this.l?(this.j.push(a),this.h[a+1]=function(){}):(c&&Ib(c,a),delete this.h[a],delete this.h[a+1],delete this.h[a+2])}return!!b};
m.Ya=function(a,b){var c=this.i[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.A)for(e=0;e<c.length;e++){var g=c[e];ej(this.h[g+1],this.h[g+2],d)}else{this.l++;try{for(e=0,f=c.length;e<f&&!this.V;e++)g=c[e],this.h[g+1].apply(this.h[g+2],d)}finally{if(this.l--,0<this.j.length&&0==this.l)for(;c=this.j.pop();)this.Bb(c)}}return 0!=e}return!1};
function ej(a,b,c){Rd(function(){a.apply(b,c)})}
m.clear=function(a){if(a){var b=this.i[a];b&&(b.forEach(this.Bb,this),delete this.i[a])}else this.h.length=0,this.i={}};
m.U=function(){M.Ba.U.call(this);this.clear();this.j.length=0};function fj(a){this.h=a}
fj.prototype.set=function(a,b){void 0===b?this.h.remove(a):this.h.set(a,(new $h).serialize(b))};
fj.prototype.get=function(a){try{var b=this.h.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
fj.prototype.remove=function(a){this.h.remove(a)};function gj(a){this.h=a}
$a(gj,fj);function hj(a){this.data=a}
function ij(a){return void 0===a||a instanceof hj?a:new hj(a)}
gj.prototype.set=function(a,b){gj.Ba.set.call(this,a,ij(b))};
gj.prototype.i=function(a){a=gj.Ba.get.call(this,a);if(void 0===a||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
gj.prototype.get=function(a){if(a=this.i(a)){if(a=a.data,void 0===a)throw"Storage: Invalid value was encountered";}else a=void 0;return a};function jj(a){this.h=a}
$a(jj,gj);jj.prototype.set=function(a,b,c){if(b=ij(b)){if(c){if(c<Za()){jj.prototype.remove.call(this,a);return}b.expiration=c}b.creation=Za()}jj.Ba.set.call(this,a,b)};
jj.prototype.i=function(a){var b=jj.Ba.i.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<Za()||c&&c>Za())jj.prototype.remove.call(this,a);else return b}};function kj(){}
;function lj(){}
$a(lj,kj);lj.prototype[Symbol.iterator]=function(){return aj(this.mb(!0)).i()};
lj.prototype.clear=function(){var a=Array.from(this);a=x(a);for(var b=a.next();!b.done;b=a.next())this.remove(b.value)};function mj(a){this.h=a;this.i=null}
$a(mj,lj);m=mj.prototype;m.isAvailable=function(){var a=this.h;if(a)try{a.setItem("__sak","1");a.removeItem("__sak");var b=!0}catch(c){b=c instanceof DOMException&&("QuotaExceededError"===c.name||22===c.code||1014===c.code||"NS_ERROR_DOM_QUOTA_REACHED"===c.name)&&a&&0!==a.length}else b=!1;return this.i=b};
m.set=function(a,b){nj(this);try{this.h.setItem(a,b)}catch(c){if(0==this.h.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
m.get=function(a){nj(this);a=this.h.getItem(a);if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
m.remove=function(a){nj(this);this.h.removeItem(a)};
m.mb=function(a){nj(this);var b=0,c=this.h,d=new Zi;d.next=function(){if(b>=c.length)return $i;var e=c.key(b++);if(a)return{value:e,done:!1};e=c.getItem(e);if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return{value:e,done:!1}};
return d};
m.clear=function(){nj(this);this.h.clear()};
m.key=function(a){nj(this);return this.h.key(a)};
function nj(a){if(null==a.h)throw Error("Storage mechanism: Storage unavailable");var b;(null!=(b=a.i)?b:a.isAvailable())||Kd(Error("Storage mechanism: Storage unavailable"))}
;function oj(){var a=null;try{a=B.localStorage||null}catch(b){}mj.call(this,a)}
$a(oj,mj);function pj(a,b){this.i=a;this.h=b+"::"}
$a(pj,lj);pj.prototype.set=function(a,b){this.i.set(this.h+a,b)};
pj.prototype.get=function(a){return this.i.get(this.h+a)};
pj.prototype.remove=function(a){this.i.remove(this.h+a)};
pj.prototype.mb=function(a){var b=this.i[Symbol.iterator](),c=this,d=new Zi;d.next=function(){var e=b.next();if(e.done)return e;for(e=e.value;e.slice(0,c.h.length)!=c.h;){e=b.next();if(e.done)return e;e=e.value}return{value:a?e.slice(c.h.length):c.i.get(e),done:!1}};
return d};/*

 (The MIT License)

 Copyright (C) 2014 by Vitaly Puzrin

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.

 -----------------------------------------------------------------------------
 Ported from zlib, which is under the following license
 https://github.com/madler/zlib/blob/master/zlib.h

 zlib.h -- interface of the 'zlib' general purpose compression library
   version 1.2.8, April 28th, 2013
   Copyright (C) 1995-2013 Jean-loup Gailly and Mark Adler
   This software is provided 'as-is', without any express or implied
   warranty.  In no event will the authors be held liable for any damages
   arising from the use of this software.
   Permission is granted to anyone to use this software for any purpose,
   including commercial applications, and to alter it and redistribute it
   freely, subject to the following restrictions:
   1. The origin of this software must not be misrepresented; you must not
      claim that you wrote the original software. If you use this software
      in a product, an acknowledgment in the product documentation would be
      appreciated but is not required.
   2. Altered source versions must be plainly marked as such, and must not be
      misrepresented as being the original software.
   3. This notice may not be removed or altered from any source distribution.
   Jean-loup Gailly        Mark Adler
   jloup@gzip.org          madler@alumni.caltech.edu
   The data format used by the zlib library is described by RFCs (Request for
   Comments) 1950 to 1952 in the files http://tools.ietf.org/html/rfc1950
   (zlib format), rfc1951 (deflate format) and rfc1952 (gzip format).
*/
var O={},qj="undefined"!==typeof Uint8Array&&"undefined"!==typeof Uint16Array&&"undefined"!==typeof Int32Array;O.assign=function(a){for(var b=Array.prototype.slice.call(arguments,1);b.length;){var c=b.shift();if(c){if("object"!==typeof c)throw new TypeError(c+"must be non-object");for(var d in c)Object.prototype.hasOwnProperty.call(c,d)&&(a[d]=c[d])}}return a};
O.Nc=function(a,b){if(a.length===b)return a;if(a.subarray)return a.subarray(0,b);a.length=b;return a};
var rj={nb:function(a,b,c,d,e){if(b.subarray&&a.subarray)a.set(b.subarray(c,c+d),e);else for(var f=0;f<d;f++)a[e+f]=b[c+f]},
cd:function(a){var b,c;var d=c=0;for(b=a.length;d<b;d++)c+=a[d].length;var e=new Uint8Array(c);d=c=0;for(b=a.length;d<b;d++){var f=a[d];e.set(f,c);c+=f.length}return e}},sj={nb:function(a,b,c,d,e){for(var f=0;f<d;f++)a[e+f]=b[c+f]},
cd:function(a){return[].concat.apply([],a)}};
O.Ye=function(){qj?(O.lb=Uint8Array,O.Ja=Uint16Array,O.Id=Int32Array,O.assign(O,rj)):(O.lb=Array,O.Ja=Array,O.Id=Array,O.assign(O,sj))};
O.Ye();var tj=!0;try{new Uint8Array(1)}catch(a){tj=!1}
function uj(a){var b,c,d=a.length,e=0;for(b=0;b<d;b++){var f=a.charCodeAt(b);if(55296===(f&64512)&&b+1<d){var g=a.charCodeAt(b+1);56320===(g&64512)&&(f=65536+(f-55296<<10)+(g-56320),b++)}e+=128>f?1:2048>f?2:65536>f?3:4}var h=new O.lb(e);for(b=c=0;c<e;b++)f=a.charCodeAt(b),55296===(f&64512)&&b+1<d&&(g=a.charCodeAt(b+1),56320===(g&64512)&&(f=65536+(f-55296<<10)+(g-56320),b++)),128>f?h[c++]=f:(2048>f?h[c++]=192|f>>>6:(65536>f?h[c++]=224|f>>>12:(h[c++]=240|f>>>18,h[c++]=128|f>>>12&63),h[c++]=128|f>>>
6&63),h[c++]=128|f&63);return h}
;var vj={};vj=function(a,b,c,d){var e=a&65535|0;a=a>>>16&65535|0;for(var f;0!==c;){f=2E3<c?2E3:c;c-=f;do e=e+b[d++]|0,a=a+e|0;while(--f);e%=65521;a%=65521}return e|a<<16|0};for(var wj={},xj,yj=[],zj=0;256>zj;zj++){xj=zj;for(var Aj=0;8>Aj;Aj++)xj=xj&1?3988292384^xj>>>1:xj>>>1;yj[zj]=xj}wj=function(a,b,c,d){c=d+c;for(a^=-1;d<c;d++)a=a>>>8^yj[(a^b[d])&255];return a^-1};var Bj={};Bj={2:"need dictionary",1:"stream end",0:"","-1":"file error","-2":"stream error","-3":"data error","-4":"insufficient memory","-5":"buffer error","-6":"incompatible version"};function Cj(a){for(var b=a.length;0<=--b;)a[b]=0}
var Dj=[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0],Ej=[0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13],Fj=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,7],Gj=[16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15],Hj=Array(576);Cj(Hj);var Ij=Array(60);Cj(Ij);var Jj=Array(512);Cj(Jj);var Kj=Array(256);Cj(Kj);var Lj=Array(29);Cj(Lj);var Mj=Array(30);Cj(Mj);function Nj(a,b,c,d,e){this.Ad=a;this.ae=b;this.Zd=c;this.Ud=d;this.xe=e;this.gd=a&&a.length}
var Oj,Pj,Qj;function Rj(a,b){this.bd=a;this.vb=0;this.Wa=b}
function Sj(a,b){a.Z[a.pending++]=b&255;a.Z[a.pending++]=b>>>8&255}
function Tj(a,b,c){a.ia>16-c?(a.oa|=b<<a.ia&65535,Sj(a,a.oa),a.oa=b>>16-a.ia,a.ia+=c-16):(a.oa|=b<<a.ia&65535,a.ia+=c)}
function Uj(a,b,c){Tj(a,c[2*b],c[2*b+1])}
function Vj(a,b){var c=0;do c|=a&1,a>>>=1,c<<=1;while(0<--b);return c>>>1}
function Wj(a,b,c){var d=Array(16),e=0,f;for(f=1;15>=f;f++)d[f]=e=e+c[f-1]<<1;for(c=0;c<=b;c++)e=a[2*c+1],0!==e&&(a[2*c]=Vj(d[e]++,e))}
function Xj(a){var b;for(b=0;286>b;b++)a.ra[2*b]=0;for(b=0;30>b;b++)a.bb[2*b]=0;for(b=0;19>b;b++)a.ka[2*b]=0;a.ra[512]=1;a.Pa=a.zb=0;a.ya=a.matches=0}
function Yj(a){8<a.ia?Sj(a,a.oa):0<a.ia&&(a.Z[a.pending++]=a.oa);a.oa=0;a.ia=0}
function Zj(a,b,c){Yj(a);Sj(a,c);Sj(a,~c);O.nb(a.Z,a.window,b,c,a.pending);a.pending+=c}
function ak(a,b,c,d){var e=2*b,f=2*c;return a[e]<a[f]||a[e]===a[f]&&d[b]<=d[c]}
function bk(a,b,c){for(var d=a.aa[c],e=c<<1;e<=a.Na;){e<a.Na&&ak(b,a.aa[e+1],a.aa[e],a.depth)&&e++;if(ak(b,d,a.aa[e],a.depth))break;a.aa[c]=a.aa[e];c=e;e<<=1}a.aa[c]=d}
function ck(a,b,c){var d=0;if(0!==a.ya){do{var e=a.Z[a.Gb+2*d]<<8|a.Z[a.Gb+2*d+1];var f=a.Z[a.Bc+d];d++;if(0===e)Uj(a,f,b);else{var g=Kj[f];Uj(a,g+256+1,b);var h=Dj[g];0!==h&&(f-=Lj[g],Tj(a,f,h));e--;g=256>e?Jj[e]:Jj[256+(e>>>7)];Uj(a,g,c);h=Ej[g];0!==h&&(e-=Mj[g],Tj(a,e,h))}}while(d<a.ya)}Uj(a,256,b)}
function dk(a,b){var c=b.bd,d=b.Wa.Ad,e=b.Wa.gd,f=b.Wa.Ud,g,h=-1;a.Na=0;a.qb=573;for(g=0;g<f;g++)0!==c[2*g]?(a.aa[++a.Na]=h=g,a.depth[g]=0):c[2*g+1]=0;for(;2>a.Na;){var k=a.aa[++a.Na]=2>h?++h:0;c[2*k]=1;a.depth[k]=0;a.Pa--;e&&(a.zb-=d[2*k+1])}b.vb=h;for(g=a.Na>>1;1<=g;g--)bk(a,c,g);k=f;do g=a.aa[1],a.aa[1]=a.aa[a.Na--],bk(a,c,1),d=a.aa[1],a.aa[--a.qb]=g,a.aa[--a.qb]=d,c[2*k]=c[2*g]+c[2*d],a.depth[k]=(a.depth[g]>=a.depth[d]?a.depth[g]:a.depth[d])+1,c[2*g+1]=c[2*d+1]=k,a.aa[1]=k++,bk(a,c,1);while(2<=
a.Na);a.aa[--a.qb]=a.aa[1];g=b.bd;k=b.vb;d=b.Wa.Ad;e=b.Wa.gd;f=b.Wa.ae;var l=b.Wa.Zd,n=b.Wa.xe,p,r=0;for(p=0;15>=p;p++)a.Ka[p]=0;g[2*a.aa[a.qb]+1]=0;for(b=a.qb+1;573>b;b++){var t=a.aa[b];p=g[2*g[2*t+1]+1]+1;p>n&&(p=n,r++);g[2*t+1]=p;if(!(t>k)){a.Ka[p]++;var v=0;t>=l&&(v=f[t-l]);var w=g[2*t];a.Pa+=w*(p+v);e&&(a.zb+=w*(d[2*t+1]+v))}}if(0!==r){do{for(p=n-1;0===a.Ka[p];)p--;a.Ka[p]--;a.Ka[p+1]+=2;a.Ka[n]--;r-=2}while(0<r);for(p=n;0!==p;p--)for(t=a.Ka[p];0!==t;)d=a.aa[--b],d>k||(g[2*d+1]!==p&&(a.Pa+=(p-
g[2*d+1])*g[2*d],g[2*d+1]=p),t--)}Wj(c,h,a.Ka)}
function ek(a,b,c){var d,e=-1,f=b[1],g=0,h=7,k=4;0===f&&(h=138,k=3);b[2*(c+1)+1]=65535;for(d=0;d<=c;d++){var l=f;f=b[2*(d+1)+1];++g<h&&l===f||(g<k?a.ka[2*l]+=g:0!==l?(l!==e&&a.ka[2*l]++,a.ka[32]++):10>=g?a.ka[34]++:a.ka[36]++,g=0,e=l,0===f?(h=138,k=3):l===f?(h=6,k=3):(h=7,k=4))}}
function fk(a,b,c){var d,e=-1,f=b[1],g=0,h=7,k=4;0===f&&(h=138,k=3);for(d=0;d<=c;d++){var l=f;f=b[2*(d+1)+1];if(!(++g<h&&l===f)){if(g<k){do Uj(a,l,a.ka);while(0!==--g)}else 0!==l?(l!==e&&(Uj(a,l,a.ka),g--),Uj(a,16,a.ka),Tj(a,g-3,2)):10>=g?(Uj(a,17,a.ka),Tj(a,g-3,3)):(Uj(a,18,a.ka),Tj(a,g-11,7));g=0;e=l;0===f?(h=138,k=3):l===f?(h=6,k=3):(h=7,k=4)}}}
function gk(a){var b=4093624447,c;for(c=0;31>=c;c++,b>>>=1)if(b&1&&0!==a.ra[2*c])return 0;if(0!==a.ra[18]||0!==a.ra[20]||0!==a.ra[26])return 1;for(c=32;256>c;c++)if(0!==a.ra[2*c])return 1;return 0}
var hk=!1;function ik(a,b,c){a.Z[a.Gb+2*a.ya]=b>>>8&255;a.Z[a.Gb+2*a.ya+1]=b&255;a.Z[a.Bc+a.ya]=c&255;a.ya++;0===b?a.ra[2*c]++:(a.matches++,b--,a.ra[2*(Kj[c]+256+1)]++,a.bb[2*(256>b?Jj[b]:Jj[256+(b>>>7)])]++);return a.ya===a.Mb-1}
;function jk(a,b){a.msg=Bj[b];return b}
function kk(a){for(var b=a.length;0<=--b;)a[b]=0}
function lk(a){var b=a.state,c=b.pending;c>a.M&&(c=a.M);0!==c&&(O.nb(a.output,b.Z,b.Pb,c,a.wb),a.wb+=c,b.Pb+=c,a.Oc+=c,a.M-=c,b.pending-=c,0===b.pending&&(b.Pb=0))}
function mk(a,b){var c=0<=a.ta?a.ta:-1,d=a.o-a.ta,e=0;if(0<a.level){2===a.I.wc&&(a.I.wc=gk(a));dk(a,a.jc);dk(a,a.dc);ek(a,a.ra,a.jc.vb);ek(a,a.bb,a.dc.vb);dk(a,a.Uc);for(e=18;3<=e&&0===a.ka[2*Gj[e]+1];e--);a.Pa+=3*(e+1)+14;var f=a.Pa+3+7>>>3;var g=a.zb+3+7>>>3;g<=f&&(f=g)}else f=g=d+5;if(d+4<=f&&-1!==c)Tj(a,b?1:0,3),Zj(a,c,d);else if(4===a.strategy||g===f)Tj(a,2+(b?1:0),3),ck(a,Hj,Ij);else{Tj(a,4+(b?1:0),3);c=a.jc.vb+1;d=a.dc.vb+1;e+=1;Tj(a,c-257,5);Tj(a,d-1,5);Tj(a,e-4,4);for(f=0;f<e;f++)Tj(a,a.ka[2*
Gj[f]+1],3);fk(a,a.ra,c-1);fk(a,a.bb,d-1);ck(a,a.ra,a.bb)}Xj(a);b&&Yj(a);a.ta=a.o;lk(a.I)}
function R(a,b){a.Z[a.pending++]=b}
function nk(a,b){a.Z[a.pending++]=b>>>8&255;a.Z[a.pending++]=b&255}
function ok(a,b){var c=a.ld,d=a.o,e=a.wa,f=a.md,g=a.o>a.ma-262?a.o-(a.ma-262):0,h=a.window,k=a.Xa,l=a.Ia,n=a.o+258,p=h[d+e-1],r=h[d+e];a.wa>=a.ed&&(c>>=2);f>a.u&&(f=a.u);do{var t=b;if(h[t+e]===r&&h[t+e-1]===p&&h[t]===h[d]&&h[++t]===h[d+1]){d+=2;for(t++;h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&h[++d]===h[++t]&&d<n;);t=258-(n-d);d=n-258;if(t>e){a.ub=b;e=t;if(t>=f)break;p=h[d+e-1];r=h[d+e]}}}while((b=l[b&k])>g&&0!==--c);return e<=
a.u?e:a.u}
function pk(a){var b=a.ma,c;do{var d=a.Gd-a.u-a.o;if(a.o>=b+(b-262)){O.nb(a.window,a.window,b,b,0);a.ub-=b;a.o-=b;a.ta-=b;var e=c=a.ic;do{var f=a.head[--e];a.head[e]=f>=b?f-b:0}while(--c);e=c=b;do f=a.Ia[--e],a.Ia[e]=f>=b?f-b:0;while(--c);d+=b}if(0===a.I.na)break;e=a.I;c=a.window;f=a.o+a.u;var g=e.na;g>d&&(g=d);0===g?c=0:(e.na-=g,O.nb(c,e.input,e.hb,g,f),1===e.state.wrap?e.H=vj(e.H,c,g,f):2===e.state.wrap&&(e.H=wj(e.H,c,g,f)),e.hb+=g,e.kb+=g,c=g);a.u+=c;if(3<=a.u+a.sa)for(d=a.o-a.sa,a.J=a.window[d],
a.J=(a.J<<a.Ma^a.window[d+1])&a.La;a.sa&&!(a.J=(a.J<<a.Ma^a.window[d+3-1])&a.La,a.Ia[d&a.Xa]=a.head[a.J],a.head[a.J]=d,d++,a.sa--,3>a.u+a.sa););}while(262>a.u&&0!==a.I.na)}
function qk(a,b){for(var c;;){if(262>a.u){pk(a);if(262>a.u&&0===b)return 1;if(0===a.u)break}c=0;3<=a.u&&(a.J=(a.J<<a.Ma^a.window[a.o+3-1])&a.La,c=a.Ia[a.o&a.Xa]=a.head[a.J],a.head[a.J]=a.o);0!==c&&a.o-c<=a.ma-262&&(a.P=ok(a,c));if(3<=a.P)if(c=ik(a,a.o-a.ub,a.P-3),a.u-=a.P,a.P<=a.Dc&&3<=a.u){a.P--;do a.o++,a.J=(a.J<<a.Ma^a.window[a.o+3-1])&a.La,a.Ia[a.o&a.Xa]=a.head[a.J],a.head[a.J]=a.o;while(0!==--a.P);a.o++}else a.o+=a.P,a.P=0,a.J=a.window[a.o],a.J=(a.J<<a.Ma^a.window[a.o+1])&a.La;else c=ik(a,0,
a.window[a.o]),a.u--,a.o++;if(c&&(mk(a,!1),0===a.I.M))return 1}a.sa=2>a.o?a.o:2;return 4===b?(mk(a,!0),0===a.I.M?3:4):a.ya&&(mk(a,!1),0===a.I.M)?1:2}
function rk(a,b){for(var c,d;;){if(262>a.u){pk(a);if(262>a.u&&0===b)return 1;if(0===a.u)break}c=0;3<=a.u&&(a.J=(a.J<<a.Ma^a.window[a.o+3-1])&a.La,c=a.Ia[a.o&a.Xa]=a.head[a.J],a.head[a.J]=a.o);a.wa=a.P;a.pd=a.ub;a.P=2;0!==c&&a.wa<a.Dc&&a.o-c<=a.ma-262&&(a.P=ok(a,c),5>=a.P&&(1===a.strategy||3===a.P&&4096<a.o-a.ub)&&(a.P=2));if(3<=a.wa&&a.P<=a.wa){d=a.o+a.u-3;c=ik(a,a.o-1-a.pd,a.wa-3);a.u-=a.wa-1;a.wa-=2;do++a.o<=d&&(a.J=(a.J<<a.Ma^a.window[a.o+3-1])&a.La,a.Ia[a.o&a.Xa]=a.head[a.J],a.head[a.J]=a.o);
while(0!==--a.wa);a.fb=0;a.P=2;a.o++;if(c&&(mk(a,!1),0===a.I.M))return 1}else if(a.fb){if((c=ik(a,0,a.window[a.o-1]))&&mk(a,!1),a.o++,a.u--,0===a.I.M)return 1}else a.fb=1,a.o++,a.u--}a.fb&&(ik(a,0,a.window[a.o-1]),a.fb=0);a.sa=2>a.o?a.o:2;return 4===b?(mk(a,!0),0===a.I.M?3:4):a.ya&&(mk(a,!1),0===a.I.M)?1:2}
function sk(a,b){for(var c,d,e,f=a.window;;){if(258>=a.u){pk(a);if(258>=a.u&&0===b)return 1;if(0===a.u)break}a.P=0;if(3<=a.u&&0<a.o&&(d=a.o-1,c=f[d],c===f[++d]&&c===f[++d]&&c===f[++d])){for(e=a.o+258;c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&d<e;);a.P=258-(e-d);a.P>a.u&&(a.P=a.u)}3<=a.P?(c=ik(a,1,a.P-3),a.u-=a.P,a.o+=a.P,a.P=0):(c=ik(a,0,a.window[a.o]),a.u--,a.o++);if(c&&(mk(a,!1),0===a.I.M))return 1}a.sa=0;return 4===b?(mk(a,!0),0===a.I.M?3:4):
a.ya&&(mk(a,!1),0===a.I.M)?1:2}
function tk(a,b){for(var c;;){if(0===a.u&&(pk(a),0===a.u)){if(0===b)return 1;break}a.P=0;c=ik(a,0,a.window[a.o]);a.u--;a.o++;if(c&&(mk(a,!1),0===a.I.M))return 1}a.sa=0;return 4===b?(mk(a,!0),0===a.I.M?3:4):a.ya&&(mk(a,!1),0===a.I.M)?1:2}
function uk(a,b,c,d,e){this.he=a;this.we=b;this.ze=c;this.ue=d;this.ce=e}
var vk;vk=[new uk(0,0,0,0,function(a,b){var c=65535;for(c>a.za-5&&(c=a.za-5);;){if(1>=a.u){pk(a);if(0===a.u&&0===b)return 1;if(0===a.u)break}a.o+=a.u;a.u=0;var d=a.ta+c;if(0===a.o||a.o>=d)if(a.u=a.o-d,a.o=d,mk(a,!1),0===a.I.M)return 1;if(a.o-a.ta>=a.ma-262&&(mk(a,!1),0===a.I.M))return 1}a.sa=0;if(4===b)return mk(a,!0),0===a.I.M?3:4;a.o>a.ta&&mk(a,!1);return 1}),
new uk(4,4,8,4,qk),new uk(4,5,16,8,qk),new uk(4,6,32,32,qk),new uk(4,4,16,16,rk),new uk(8,16,32,32,rk),new uk(8,16,128,128,rk),new uk(8,32,128,256,rk),new uk(32,128,258,1024,rk),new uk(32,258,258,4096,rk)];
function wk(){this.I=null;this.status=0;this.Z=null;this.wrap=this.pending=this.Pb=this.za=0;this.G=null;this.Ca=0;this.method=8;this.sb=-1;this.Xa=this.Rc=this.ma=0;this.window=null;this.Gd=0;this.head=this.Ia=null;this.md=this.ed=this.strategy=this.level=this.Dc=this.ld=this.wa=this.u=this.ub=this.o=this.fb=this.pd=this.P=this.ta=this.Ma=this.La=this.zc=this.ic=this.J=0;this.ra=new O.Ja(1146);this.bb=new O.Ja(122);this.ka=new O.Ja(78);kk(this.ra);kk(this.bb);kk(this.ka);this.Uc=this.dc=this.jc=
null;this.Ka=new O.Ja(16);this.aa=new O.Ja(573);kk(this.aa);this.qb=this.Na=0;this.depth=new O.Ja(573);kk(this.depth);this.ia=this.oa=this.sa=this.matches=this.zb=this.Pa=this.Gb=this.ya=this.Mb=this.Bc=0}
function xk(a,b){if(!a||!a.state||5<b||0>b)return a?jk(a,-2):-2;var c=a.state;if(!a.output||!a.input&&0!==a.na||666===c.status&&4!==b)return jk(a,0===a.M?-5:-2);c.I=a;var d=c.sb;c.sb=b;if(42===c.status)if(2===c.wrap)a.H=0,R(c,31),R(c,139),R(c,8),c.G?(R(c,(c.G.text?1:0)+(c.G.Ta?2:0)+(c.G.extra?4:0)+(c.G.name?8:0)+(c.G.comment?16:0)),R(c,c.G.time&255),R(c,c.G.time>>8&255),R(c,c.G.time>>16&255),R(c,c.G.time>>24&255),R(c,9===c.level?2:2<=c.strategy||2>c.level?4:0),R(c,c.G.os&255),c.G.extra&&c.G.extra.length&&
(R(c,c.G.extra.length&255),R(c,c.G.extra.length>>8&255)),c.G.Ta&&(a.H=wj(a.H,c.Z,c.pending,0)),c.Ca=0,c.status=69):(R(c,0),R(c,0),R(c,0),R(c,0),R(c,0),R(c,9===c.level?2:2<=c.strategy||2>c.level?4:0),R(c,3),c.status=113);else{var e=8+(c.Rc-8<<4)<<8;e|=(2<=c.strategy||2>c.level?0:6>c.level?1:6===c.level?2:3)<<6;0!==c.o&&(e|=32);c.status=113;nk(c,e+(31-e%31));0!==c.o&&(nk(c,a.H>>>16),nk(c,a.H&65535));a.H=1}if(69===c.status)if(c.G.extra){for(e=c.pending;c.Ca<(c.G.extra.length&65535)&&(c.pending!==c.za||
(c.G.Ta&&c.pending>e&&(a.H=wj(a.H,c.Z,c.pending-e,e)),lk(a),e=c.pending,c.pending!==c.za));)R(c,c.G.extra[c.Ca]&255),c.Ca++;c.G.Ta&&c.pending>e&&(a.H=wj(a.H,c.Z,c.pending-e,e));c.Ca===c.G.extra.length&&(c.Ca=0,c.status=73)}else c.status=73;if(73===c.status)if(c.G.name){e=c.pending;do{if(c.pending===c.za&&(c.G.Ta&&c.pending>e&&(a.H=wj(a.H,c.Z,c.pending-e,e)),lk(a),e=c.pending,c.pending===c.za)){var f=1;break}f=c.Ca<c.G.name.length?c.G.name.charCodeAt(c.Ca++)&255:0;R(c,f)}while(0!==f);c.G.Ta&&c.pending>
e&&(a.H=wj(a.H,c.Z,c.pending-e,e));0===f&&(c.Ca=0,c.status=91)}else c.status=91;if(91===c.status)if(c.G.comment){e=c.pending;do{if(c.pending===c.za&&(c.G.Ta&&c.pending>e&&(a.H=wj(a.H,c.Z,c.pending-e,e)),lk(a),e=c.pending,c.pending===c.za)){f=1;break}f=c.Ca<c.G.comment.length?c.G.comment.charCodeAt(c.Ca++)&255:0;R(c,f)}while(0!==f);c.G.Ta&&c.pending>e&&(a.H=wj(a.H,c.Z,c.pending-e,e));0===f&&(c.status=103)}else c.status=103;103===c.status&&(c.G.Ta?(c.pending+2>c.za&&lk(a),c.pending+2<=c.za&&(R(c,a.H&
255),R(c,a.H>>8&255),a.H=0,c.status=113)):c.status=113);if(0!==c.pending){if(lk(a),0===a.M)return c.sb=-1,0}else if(0===a.na&&(b<<1)-(4<b?9:0)<=(d<<1)-(4<d?9:0)&&4!==b)return jk(a,-5);if(666===c.status&&0!==a.na)return jk(a,-5);if(0!==a.na||0!==c.u||0!==b&&666!==c.status){d=2===c.strategy?tk(c,b):3===c.strategy?sk(c,b):vk[c.level].ce(c,b);if(3===d||4===d)c.status=666;if(1===d||3===d)return 0===a.M&&(c.sb=-1),0;if(2===d&&(1===b?(Tj(c,2,3),Uj(c,256,Hj),16===c.ia?(Sj(c,c.oa),c.oa=0,c.ia=0):8<=c.ia&&
(c.Z[c.pending++]=c.oa&255,c.oa>>=8,c.ia-=8)):5!==b&&(Tj(c,0,3),Zj(c,0,0),3===b&&(kk(c.head),0===c.u&&(c.o=0,c.ta=0,c.sa=0))),lk(a),0===a.M))return c.sb=-1,0}if(4!==b)return 0;if(0>=c.wrap)return 1;2===c.wrap?(R(c,a.H&255),R(c,a.H>>8&255),R(c,a.H>>16&255),R(c,a.H>>24&255),R(c,a.kb&255),R(c,a.kb>>8&255),R(c,a.kb>>16&255),R(c,a.kb>>24&255)):(nk(c,a.H>>>16),nk(c,a.H&65535));lk(a);0<c.wrap&&(c.wrap=-c.wrap);return 0!==c.pending?0:1}
;var yk={};yk=function(){this.input=null;this.kb=this.na=this.hb=0;this.output=null;this.Oc=this.M=this.wb=0;this.msg="";this.state=null;this.wc=2;this.H=0};var zk=Object.prototype.toString;
function Ak(a){if(!(this instanceof Ak))return new Ak(a);a=this.options=O.assign({level:-1,method:8,chunkSize:16384,windowBits:15,memLevel:8,strategy:0,to:""},a||{});a.raw&&0<a.windowBits?a.windowBits=-a.windowBits:a.gzip&&0<a.windowBits&&16>a.windowBits&&(a.windowBits+=16);this.err=0;this.msg="";this.ended=!1;this.chunks=[];this.I=new yk;this.I.M=0;var b=this.I;var c=a.level,d=a.method,e=a.windowBits,f=a.memLevel,g=a.strategy;if(b){var h=1;-1===c&&(c=6);0>e?(h=0,e=-e):15<e&&(h=2,e-=16);if(1>f||9<
f||8!==d||8>e||15<e||0>c||9<c||0>g||4<g)b=jk(b,-2);else{8===e&&(e=9);var k=new wk;b.state=k;k.I=b;k.wrap=h;k.G=null;k.Rc=e;k.ma=1<<k.Rc;k.Xa=k.ma-1;k.zc=f+7;k.ic=1<<k.zc;k.La=k.ic-1;k.Ma=~~((k.zc+3-1)/3);k.window=new O.lb(2*k.ma);k.head=new O.Ja(k.ic);k.Ia=new O.Ja(k.ma);k.Mb=1<<f+6;k.za=4*k.Mb;k.Z=new O.lb(k.za);k.Gb=1*k.Mb;k.Bc=3*k.Mb;k.level=c;k.strategy=g;k.method=d;if(b&&b.state){b.kb=b.Oc=0;b.wc=2;c=b.state;c.pending=0;c.Pb=0;0>c.wrap&&(c.wrap=-c.wrap);c.status=c.wrap?42:113;b.H=2===c.wrap?
0:1;c.sb=0;if(!hk){d=Array(16);for(f=g=0;28>f;f++)for(Lj[f]=g,e=0;e<1<<Dj[f];e++)Kj[g++]=f;Kj[g-1]=f;for(f=g=0;16>f;f++)for(Mj[f]=g,e=0;e<1<<Ej[f];e++)Jj[g++]=f;for(g>>=7;30>f;f++)for(Mj[f]=g<<7,e=0;e<1<<Ej[f]-7;e++)Jj[256+g++]=f;for(e=0;15>=e;e++)d[e]=0;for(e=0;143>=e;)Hj[2*e+1]=8,e++,d[8]++;for(;255>=e;)Hj[2*e+1]=9,e++,d[9]++;for(;279>=e;)Hj[2*e+1]=7,e++,d[7]++;for(;287>=e;)Hj[2*e+1]=8,e++,d[8]++;Wj(Hj,287,d);for(e=0;30>e;e++)Ij[2*e+1]=5,Ij[2*e]=Vj(e,5);Oj=new Nj(Hj,Dj,257,286,15);Pj=new Nj(Ij,
Ej,0,30,15);Qj=new Nj([],Fj,0,19,7);hk=!0}c.jc=new Rj(c.ra,Oj);c.dc=new Rj(c.bb,Pj);c.Uc=new Rj(c.ka,Qj);c.oa=0;c.ia=0;Xj(c);c=0}else c=jk(b,-2);0===c&&(b=b.state,b.Gd=2*b.ma,kk(b.head),b.Dc=vk[b.level].we,b.ed=vk[b.level].he,b.md=vk[b.level].ze,b.ld=vk[b.level].ue,b.o=0,b.ta=0,b.u=0,b.sa=0,b.P=b.wa=2,b.fb=0,b.J=0);b=c}}else b=-2;if(0!==b)throw Error(Bj[b]);a.header&&(b=this.I)&&b.state&&2===b.state.wrap&&(b.state.G=a.header);if(a.dictionary){var l;"string"===typeof a.dictionary?l=uj(a.dictionary):
"[object ArrayBuffer]"===zk.call(a.dictionary)?l=new Uint8Array(a.dictionary):l=a.dictionary;a=this.I;f=l;g=f.length;if(a&&a.state)if(l=a.state,b=l.wrap,2===b||1===b&&42!==l.status||l.u)b=-2;else{1===b&&(a.H=vj(a.H,f,g,0));l.wrap=0;g>=l.ma&&(0===b&&(kk(l.head),l.o=0,l.ta=0,l.sa=0),c=new O.lb(l.ma),O.nb(c,f,g-l.ma,l.ma,0),f=c,g=l.ma);c=a.na;d=a.hb;e=a.input;a.na=g;a.hb=0;a.input=f;for(pk(l);3<=l.u;){f=l.o;g=l.u-2;do l.J=(l.J<<l.Ma^l.window[f+3-1])&l.La,l.Ia[f&l.Xa]=l.head[l.J],l.head[l.J]=f,f++;while(--g);
l.o=f;l.u=2;pk(l)}l.o+=l.u;l.ta=l.o;l.sa=l.u;l.u=0;l.P=l.wa=2;l.fb=0;a.hb=d;a.input=e;a.na=c;l.wrap=b;b=0}else b=-2;if(0!==b)throw Error(Bj[b]);this.Bg=!0}}
Ak.prototype.push=function(a,b){var c=this.I,d=this.options.chunkSize;if(this.ended)return!1;var e=b===~~b?b:!0===b?4:0;"string"===typeof a?c.input=uj(a):"[object ArrayBuffer]"===zk.call(a)?c.input=new Uint8Array(a):c.input=a;c.hb=0;c.na=c.input.length;do{0===c.M&&(c.output=new O.lb(d),c.wb=0,c.M=d);a=xk(c,e);if(1!==a&&0!==a)return Bk(this,a),this.ended=!0,!1;if(0===c.M||0===c.na&&(4===e||2===e))if("string"===this.options.to){var f=O.Nc(c.output,c.wb);b=f;f=f.length;if(65537>f&&(b.subarray&&tj||!b.subarray))b=
String.fromCharCode.apply(null,O.Nc(b,f));else{for(var g="",h=0;h<f;h++)g+=String.fromCharCode(b[h]);b=g}this.chunks.push(b)}else b=O.Nc(c.output,c.wb),this.chunks.push(b)}while((0<c.na||0===c.M)&&1!==a);if(4===e)return(c=this.I)&&c.state?(d=c.state.status,42!==d&&69!==d&&73!==d&&91!==d&&103!==d&&113!==d&&666!==d?a=jk(c,-2):(c.state=null,a=113===d?jk(c,-3):0)):a=-2,Bk(this,a),this.ended=!0,0===a;2===e&&(Bk(this,0),c.M=0);return!0};
function Bk(a,b){0===b&&(a.result="string"===a.options.to?a.chunks.join(""):O.cd(a.chunks));a.chunks=[];a.err=b;a.msg=a.I.msg}
function Ck(a,b){b=b||{};b.gzip=!0;b=new Ak(b);b.push(a,!0);if(b.err)throw b.msg||Bj[b.err];return b.result}
;function Dk(a){if(!a)return null;a=a.privateDoNotAccessOrElseTrustedResourceUrlWrappedValue;var b;a?b=mb(a):b=null;return b}
;function Ek(a){return mb(null===a?"null":void 0===a?"undefined":a)}
;function Fk(a){this.name=a}
;var Gk=new Fk("rawColdConfigGroup");var Hk=new Fk("rawHotConfigGroup");function Ik(a){this.D=I(a)}
y(Ik,L);var Jk=new Fk("continuationCommand");var Kk=new Fk("webCommandMetadata");var Lk=new Fk("signalServiceEndpoint");var Mk={Ef:"EMBEDDED_PLAYER_MODE_UNKNOWN",Bf:"EMBEDDED_PLAYER_MODE_DEFAULT",Df:"EMBEDDED_PLAYER_MODE_PFP",Cf:"EMBEDDED_PLAYER_MODE_PFL"};var Nk=new Fk("feedbackEndpoint");function Ok(a){this.D=I(a)}
y(Ok,L);Ok.prototype.setTrackingParams=function(a){if(null!=a)if("string"===typeof a)a=a?new We(a,Te):Ue||(Ue=new We(null,Te));else if(a.constructor!==We)if(Se(a))a=a.length?new We(new Uint8Array(a),Te):Ue||(Ue=new We(null,Te));else throw Error();return J(this,1,a)};var Ki={gg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_UNKNOWN",Of:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_FOR_TESTING",Wf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_RESUME_TO_HOME_TTL",ag:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_START_TO_SHORTS_ANALYSIS_SLICE",Lf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_DEVICE_LAYER_SLICE",fg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_UNIFIED_LAYER_SLICE",hg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_VISITOR_LAYER_SLICE",Zf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_SHOW_SHEET_COMMAND_HANDLER_BLOCK",
jg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WIZ_NEXT_MIGRATED_COMPONENT",ig:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WIZ_NEXT_CHANNEL_NAME_TOOLTIP",Xf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ROTATION_LOCK_SUPPORTED",dg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_THEATER_MODE_ENABLED",ng:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_SHOW_PIN_SUGGESTION",mg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_SHOW_LONG_PRESS_EDU_TOAST",lg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_SHOW_AMBIENT",eg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_TIME_WATCHED_PANEL",
Yf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_SEARCH_FROM_SEARCH_BAR_OVERLAY",og:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_SHOW_VOICE_SEARCH_EDU_TOAST",cg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_SUGGESTED_LANGUAGE_SELECTED",pg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_TRIGGER_SHORTS_PIP",Pf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_IN_ZP_VOICE_CRASHY_SET",Sf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_REEL_FAST_SWIPE_SUPPRESSED",Rf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_REEL_FAST_SWIPE_ALLOWED",Uf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_REEL_PULL_TO_REFRESH_ATTEMPT",
kg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_BLOCK_KABUKI",Vf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_REEL_TALL_SCREEN",Tf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_REEL_NORMAL_SCREEN",If:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ACCESSIBILITY_MODE_ENABLED",Hf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ACCESSIBILITY_MODE_DISABLED",Jf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_AUTOPLAY_ENABLED",Kf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_CAST_MATCH_OCCURRED",Mf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_EMC3DS_ELIGIBLE",Nf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ENDSCREEN_TRIGGERED",
Qf:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_POSTPLAY_TRIGGERED"};var Pk=new Fk("webPlayerShareEntityServiceEndpoint");var Qk=new Fk("playlistEditEndpoint");var Rk=new Fk("modifyChannelNotificationPreferenceEndpoint");var Sk=new Fk("unsubscribeEndpoint");var Tk=new Fk("subscribeEndpoint");function Uk(){var a=Vk;E("yt.ads.biscotti.getId_")||D("yt.ads.biscotti.getId_",a)}
function Wk(a){D("yt.ads.biscotti.lastId_",a)}
;function Xk(a,b){1<b.length?a[b[0]]=b[1]:1===b.length&&Object.assign(a,b[0])}
;var Yk=B.window,Zk,$k,al=(null==Yk?void 0:null==(Zk=Yk.yt)?void 0:Zk.config_)||(null==Yk?void 0:null==($k=Yk.ytcfg)?void 0:$k.data_)||{};D("yt.config_",al);function bl(){Xk(al,arguments)}
function T(a,b){return a in al?al[a]:b}
function cl(a){var b=al.EXPERIMENT_FLAGS;return b?b[a]:void 0}
;var dl=[];function el(a){dl.forEach(function(b){return b(a)})}
function fl(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){gl(b)}}:a}
function gl(a){var b=E("yt.logging.errors.log");b?b(a,"ERROR",void 0,void 0,void 0,void 0,void 0):(b=T("ERRORS",[]),b.push([a,"ERROR",void 0,void 0,void 0,void 0,void 0]),bl("ERRORS",b));el(a)}
function hl(a,b,c,d,e){var f=E("yt.logging.errors.log");f?f(a,"WARNING",b,c,d,void 0,e):(f=T("ERRORS",[]),f.push([a,"WARNING",b,c,d,void 0,e]),bl("ERRORS",f))}
;var il=/^[\w.]*$/,jl={q:!0,search_query:!0};function kl(a,b){b=a.split(b);for(var c={},d=0,e=b.length;d<e;d++){var f=b[d].split("=");if(1===f.length&&f[0]||2===f.length)try{var g=ll(f[0]||""),h=ll(f[1]||"");if(g in c){var k=c[g];Array.isArray(k)?Jb(k,h):c[g]=[k,h]}else c[g]=h}catch(r){var l=r,n=f[0],p=String(kl);l.args=[{key:n,value:f[1],query:a,method:ml===p?"unchanged":p}];jl.hasOwnProperty(n)||hl(l)}}return c}
var ml=String(kl);function nl(a){var b=[];Kb(a,function(c,d){var e=encodeURIComponent(String(d));c=Array.isArray(c)?c:[c];Db(c,function(f){""==f?b.push(e):b.push(e+"="+encodeURIComponent(String(f)))})});
return b.join("&")}
function ol(a){"?"===a.charAt(0)&&(a=a.substring(1));return kl(a,"&")}
function pl(a){return-1!==a.indexOf("?")?(a=(a||"").split("#")[0],a=a.split("?",2),ol(1<a.length?a[1]:a[0])):{}}
function ql(a,b,c){var d=a.split("#",2);a=d[0];d=1<d.length?"#"+d[1]:"";var e=a.split("?",2);a=e[0];e=ol(e[1]||"");for(var f in b)!c&&null!==e&&f in e||(e[f]=b[f]);return tc(a,e)+d}
function rl(a){if(!b)var b=window.location.href;var c=nc(1,a),d=oc(a);c&&d?(a=a.match(lc),b=b.match(lc),a=a[3]==b[3]&&a[1]==b[1]&&a[4]==b[4]):a=d?oc(b)===d&&(Number(nc(4,b))||null)===(Number(nc(4,a))||null):!0;return a}
function ll(a){return a&&a.match(il)?a:decodeURIComponent(a.replace(/\+/g," "))}
;function sl(a){var b=tl;a=void 0===a?E("yt.ads.biscotti.lastId_")||"":a;var c=Object,d=c.assign,e={};e.dt=Ii;e.flash="0";a:{try{var f=b.h.top.location.href}catch(Ka){f=2;break a}f=f?f===b.i.location.href?0:1:2}e=(e.frm=f,e);try{e.u_tz=-(new Date).getTimezoneOffset();var g=void 0===g?Ai:g;try{var h=g.history.length}catch(Ka){h=0}e.u_his=h;var k;e.u_h=null==(k=Ai.screen)?void 0:k.height;var l;e.u_w=null==(l=Ai.screen)?void 0:l.width;var n;e.u_ah=null==(n=Ai.screen)?void 0:n.availHeight;var p;e.u_aw=
null==(p=Ai.screen)?void 0:p.availWidth;var r;e.u_cd=null==(r=Ai.screen)?void 0:r.colorDepth}catch(Ka){}h=b.h;try{var t=h.screenX;var v=h.screenY}catch(Ka){}try{var w=h.outerWidth;var C=h.outerHeight}catch(Ka){}try{var F=h.innerWidth;var K=h.innerHeight}catch(Ka){}try{var N=h.screenLeft;var S=h.screenTop}catch(Ka){}try{F=h.innerWidth,K=h.innerHeight}catch(Ka){}try{var da=h.screen.availWidth;var ta=h.screen.availTop}catch(Ka){}t=[N,S,t,v,da,ta,w,C,F,K];try{var P=(b.h.top||window).document,ea="CSS1Compat"==
P.compatMode?P.documentElement:P.body;var na=(new Ed(ea.clientWidth,ea.clientHeight)).round()}catch(Ka){na=new Ed(-12245933,-12245933)}P=na;na={};var La=void 0===La?B:La;ea=new Qi;"SVGElement"in La&&"createElementNS"in La.document&&ea.set(0);v=Fi();v["allow-top-navigation-by-user-activation"]&&ea.set(1);v["allow-popups-to-escape-sandbox"]&&ea.set(2);La.crypto&&La.crypto.subtle&&ea.set(3);"TextDecoder"in La&&"TextEncoder"in La&&ea.set(4);La=Ri(ea);na.bc=La;na.bih=P.height;na.biw=P.width;na.brdim=t.join();
b=b.i;b=(na.vis=b.prerendering?3:{visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[b.visibilityState||b.webkitVisibilityState||b.mozVisibilityState||""]||0,na.wgl=!!Ai.WebGLRenderingContext,na);c=d.call(c,e,b);c.ca_type="image";a&&(c.bid=a);return c}
var tl=new function(){var a=window.document;this.h=window;this.i=a};
D("yt.ads_.signals_.getAdSignalsString",function(a){return nl(sl(a))});Za();navigator.userAgent.indexOf(" (CrKey ");var ul="XMLHttpRequest"in B?function(){return new XMLHttpRequest}:null;
function vl(){if(!ul)return null;var a=ul();return"open"in a?a:null}
function wl(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;function xl(a,b){"function"===typeof a&&(a=fl(a));return window.setTimeout(a,b)}
;var yl="client_dev_domain client_dev_expflag client_dev_regex_map client_dev_root_url client_rollout_override expflag forcedCapability jsfeat jsmode mods".split(" ");[].concat(la(yl),["client_dev_set_cookie"]);function U(a){a=zl(a);return"string"===typeof a&&"false"===a?!1:!!a}
function Al(a,b){a=zl(a);return void 0===a&&void 0!==b?b:Number(a||0)}
function zl(a){return T("EXPERIMENT_FLAGS",{})[a]}
function Bl(){for(var a=[],b=T("EXPERIMENTS_FORCED_FLAGS",{}),c=x(Object.keys(b)),d=c.next();!d.done;d=c.next())d=d.value,a.push({key:d,value:String(b[d])});c=T("EXPERIMENT_FLAGS",{});d=x(Object.keys(c));for(var e=d.next();!e.done;e=d.next())e=e.value,e.startsWith("force_")&&void 0===b[e]&&a.push({key:e,value:String(c[e])});return a}
;var Cl={Authorization:"AUTHORIZATION","X-Goog-EOM-Visitor-Id":"EOM_VISITOR_DATA","X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-Youtube-Domain-Admin-State":"DOMAIN_ADMIN_STATE","X-Youtube-Chrome-Connected":"CHROME_CONNECTED_HEADER","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-YouTube-Delegation-Context":"INNERTUBE_CONTEXT_SERIALIZED_DELEGATION_CONTEXT","X-YouTube-Device":"DEVICE","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL",
"X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM","X-Goog-AuthUser":"SESSION_INDEX","X-Goog-PageId":"DELEGATED_SESSION_ID"},Dl="app debugcss debugjs expflag force_ad_params force_ad_encrypted force_viral_ad_response_params forced_experiments innertube_snapshots innertube_goldens internalcountrycode internalipoverride absolute_experiments conditional_experiments sbb sr_bns_address".split(" ").concat(la(yl)),El=!1;
function Fl(a,b,c,d,e,f,g,h){function k(){4===(l&&"readyState"in l?l.readyState:0)&&b&&fl(b)(l)}
c=void 0===c?"GET":c;d=void 0===d?"":d;h=void 0===h?!1:h;var l=vl();if(!l)return null;"onloadend"in l?l.addEventListener("loadend",k,!1):l.onreadystatechange=k;U("debug_forward_web_query_parameters")&&(a=Gl(a));l.open(c,a,!0);f&&(l.responseType=f);g&&(l.withCredentials=!0);c="POST"===c&&(void 0===window.FormData||!(d instanceof FormData));if(e=Hl(a,e))for(var n in e)l.setRequestHeader(n,e[n]),"content-type"===n.toLowerCase()&&(c=!1);c&&l.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
if(h&&"setAttributionReporting"in XMLHttpRequest.prototype){a={eventSourceEligible:!0,triggerEligible:!1};try{l.setAttributionReporting(a)}catch(p){hl(p)}}l.send(d);return l}
function Hl(a,b){b=void 0===b?{}:b;var c=rl(a),d=U("web_ajax_ignore_global_headers_if_set"),e;for(e in Cl){var f=T(Cl[e]),g="X-Goog-AuthUser"===e||"X-Goog-PageId"===e;"X-Goog-Visitor-Id"!==e||f||(f=T("VISITOR_DATA"));!f||!c&&oc(a)||d&&void 0!==b[e]||"TVHTML5_UNPLUGGED"===T("INNERTUBE_CLIENT_NAME")&&g||(b[e]=f)}"X-Goog-EOM-Visitor-Id"in b&&"X-Goog-Visitor-Id"in b&&delete b["X-Goog-Visitor-Id"];if(c||!oc(a))b["X-YouTube-Utc-Offset"]=String(-(new Date).getTimezoneOffset());if(c||!oc(a)){try{var h=(new Intl.DateTimeFormat).resolvedOptions().timeZone}catch(k){}h&&
(b["X-YouTube-Time-Zone"]=h)}document.location.hostname.endsWith("youtubeeducation.com")||!c&&oc(a)||(b["X-YouTube-Ad-Signals"]=nl(sl()));return b}
function Il(a,b){b.method="POST";b.postParams||(b.postParams={});return Jl(a,b)}
function Jl(a,b){var c=b.format||"JSON";a=Kl(a,b);var d=Ll(a,b),e=!1,f=Ml(a,function(k){if(!e){e=!0;h&&window.clearTimeout(h);var l=wl(k),n=null,p=400<=k.status&&500>k.status,r=500<=k.status&&600>k.status;if(l||p||r)n=Nl(a,c,k,b.convertToSafeHtml);l&&(l=Ol(c,k,n));n=n||{};p=b.context||B;l?b.onSuccess&&b.onSuccess.call(p,k,n):b.onError&&b.onError.call(p,k,n);b.onFinish&&b.onFinish.call(p,k,n)}},b.method,d,b.headers,b.responseType,b.withCredentials);
d=b.timeout||0;if(b.onTimeout&&0<d){var g=b.onTimeout;var h=xl(function(){e||(e=!0,f.abort(),window.clearTimeout(h),g.call(b.context||B,f))},d)}return f}
function Kl(a,b){b.includeDomain&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=T("XSRF_FIELD_NAME");if(b=b.urlParams)b[c]&&delete b[c],a=ql(a,b||{},!0);return a}
function Ll(a,b){var c=T("XSRF_FIELD_NAME"),d=T("XSRF_TOKEN"),e=b.postBody||"",f=b.postParams,g=T("XSRF_FIELD_NAME"),h;b.headers&&(h=b.headers["Content-Type"]);b.excludeXsrf||oc(a)&&!b.withCredentials&&oc(a)!==document.location.hostname||"POST"!==b.method||h&&"application/x-www-form-urlencoded"!==h||b.postParams&&b.postParams[g]||(f||(f={}),f[c]=d);(U("ajax_parse_query_data_only_when_filled")&&f&&0<Object.keys(f).length||f)&&"string"===typeof e&&(e=ol(e),Ub(e,f),e=b.postBodyFormat&&"JSON"===b.postBodyFormat?
JSON.stringify(e):sc(e));f=e||f&&!Nb(f);!El&&f&&"POST"!==b.method&&(El=!0,gl(Error("AJAX request with postData should use POST")));return e}
function Nl(a,b,c,d){var e=null;switch(b){case "JSON":try{var f=c.responseText}catch(g){throw d=Error("Error reading responseText"),d.params=a,hl(d),g;}a=c.getResponseHeader("Content-Type")||"";f&&0<=a.indexOf("json")&&(")]}'\n"===f.substring(0,5)&&(f=f.substring(5)),e=JSON.parse(f));break;case "XML":if(a=(a=c.responseXML)?Pl(a):null)e={},Db(a.getElementsByTagName("*"),function(g){e[g.tagName]=Ql(g)})}d&&Rl(e);
return e}
function Rl(a){if(Ra(a))for(var b in a){var c;(c="html_content"===b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=a[b],e=fb();d=e?e.createHTML(d):d;a[c]=new Vb(d)}else Rl(a[b])}}
function Ol(a,b,c){if(b&&204===b.status)return!0;switch(a){case "JSON":return!!c;case "XML":return 0===Number(c&&c.return_code);case "RAW":return!0;default:return!!c}}
function Pl(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Ql(a){var b="";Db(a.childNodes,function(c){b+=c.nodeValue});
return b}
function Gl(a){var b=window.location.search,c=oc(a);U("debug_handle_relative_url_for_query_forward_killswitch")||!c&&rl(a)&&(c=document.location.hostname);var d=mc(nc(5,a));d=(c=c&&(c.endsWith("youtube.com")||c.endsWith("youtube-nocookie.com")))&&d&&d.startsWith("/api/");if(!c||d)return a;var e=ol(b),f={};Db(Dl,function(g){e[g]&&(f[g]=e[g])});
return ql(a,f||{},!1)}
var Ml=Fl;var Sl=[{Ec:function(a){return"Cannot read property '"+a.key+"'"},
kc:{Error:[{regexp:/(Permission denied) to access property "([^']+)"/,groups:["reason","key"]}],TypeError:[{regexp:/Cannot read property '([^']+)' of (null|undefined)/,groups:["key","value"]},{regexp:/\u65e0\u6cd5\u83b7\u53d6\u672a\u5b9a\u4e49\u6216 (null|undefined) \u5f15\u7528\u7684\u5c5e\u6027\u201c([^\u201d]+)\u201d/,groups:["value","key"]},{regexp:/\uc815\uc758\ub418\uc9c0 \uc54a\uc74c \ub610\ub294 (null|undefined) \ucc38\uc870\uc778 '([^']+)' \uc18d\uc131\uc744 \uac00\uc838\uc62c \uc218 \uc5c6\uc2b5\ub2c8\ub2e4./,
groups:["value","key"]},{regexp:/No se puede obtener la propiedad '([^']+)' de referencia nula o sin definir/,groups:["key"]},{regexp:/Unable to get property '([^']+)' of (undefined or null) reference/,groups:["key","value"]},{regexp:/(null) is not an object \(evaluating '(?:([^.]+)\.)?([^']+)'\)/,groups:["value","base","key"]}]}},{Ec:function(a){return"Cannot call '"+a.key+"'"},
kc:{TypeError:[{regexp:/(?:([^ ]+)?\.)?([^ ]+) is not a function/,groups:["base","key"]},{regexp:/([^ ]+) called on (null or undefined)/,groups:["key","value"]},{regexp:/Object (.*) has no method '([^ ]+)'/,groups:["base","key"]},{regexp:/Object doesn't support property or method '([^ ]+)'/,groups:["key"]},{regexp:/\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u306f '([^']+)' \u30d7\u30ed\u30d1\u30c6\u30a3\u307e\u305f\u306f\u30e1\u30bd\u30c3\u30c9\u3092\u30b5\u30dd\u30fc\u30c8\u3057\u3066\u3044\u307e\u305b\u3093/,
groups:["key"]},{regexp:/\uac1c\uccb4\uac00 '([^']+)' \uc18d\uc131\uc774\ub098 \uba54\uc11c\ub4dc\ub97c \uc9c0\uc6d0\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4./,groups:["key"]}]}},{Ec:function(a){return a.key+" is not defined"},
kc:{ReferenceError:[{regexp:/(.*) is not defined/,groups:["key"]},{regexp:/Can't find variable: (.*)/,groups:["key"]}]}}];var Ul={Va:[],Sa:[{callback:Tl,weight:500}]};function Tl(a){if("JavaException"===a.name)return!0;a=a.stack;return a.includes("chrome://")||a.includes("chrome-extension://")||a.includes("moz-extension://")}
;function Vl(){this.Sa=[];this.Va=[]}
var Wl;function Xl(){if(!Wl){var a=Wl=new Vl;a.Va.length=0;a.Sa.length=0;Ul.Va&&a.Va.push.apply(a.Va,Ul.Va);Ul.Sa&&a.Sa.push.apply(a.Sa,Ul.Sa)}return Wl}
;var Yl=new M;function Zl(a){function b(){return a.charCodeAt(d++)}
var c=a.length,d=0;do{var e=$l(b);if(Infinity===e)break;var f=e>>3;switch(e&7){case 0:e=$l(b);if(2===f)return e;break;case 1:if(2===f)return;d+=8;break;case 2:e=$l(b);if(2===f)return a.substr(d,e);d+=e;break;case 5:if(2===f)return;d+=4;break;default:return}}while(d<c)}
function $l(a){var b=a(),c=b&127;if(128>b)return c;b=a();c|=(b&127)<<7;if(128>b)return c;b=a();c|=(b&127)<<14;if(128>b)return c;b=a();return 128>b?c|(b&127)<<21:Infinity}
;function am(a,b,c,d){if(a)if(Array.isArray(a)){var e=d;for(d=0;d<a.length&&!(a[d]&&(e+=bm(d,a[d],b,c),500<e));d++);d=e}else if("object"===typeof a)for(e in a){if(a[e]){var f=e;var g=a[e],h=b,k=c;f="string"!==typeof g||"clickTrackingParams"!==f&&"trackingParams"!==f?0:(g=Zl(atob(g.replace(/-/g,"+").replace(/_/g,"/"))))?bm(f+".ve",g,h,k):0;d+=f;d+=bm(e,a[e],b,c);if(500<d)break}}else c[b]=cm(a),d+=c[b].length;else c[b]=cm(a),d+=c[b].length;return d}
function bm(a,b,c,d){c+="."+a;a=cm(b);d[c]=a;return c.length+a.length}
function cm(a){try{return("string"===typeof a?a:String(JSON.stringify(a))).substr(0,500)}catch(b){return"unable to serialize "+typeof a+" ("+b.message+")"}}
;function dm(a){var b=this;this.i=void 0;this.h=!1;a.addEventListener("beforeinstallprompt",function(c){c.preventDefault();b.i=c});
a.addEventListener("appinstalled",function(){b.h=!0},{once:!0})}
function em(){if(!B.matchMedia)return"WEB_DISPLAY_MODE_UNKNOWN";try{return B.matchMedia("(display-mode: standalone)").matches?"WEB_DISPLAY_MODE_STANDALONE":B.matchMedia("(display-mode: minimal-ui)").matches?"WEB_DISPLAY_MODE_MINIMAL_UI":B.matchMedia("(display-mode: fullscreen)").matches?"WEB_DISPLAY_MODE_FULLSCREEN":B.matchMedia("(display-mode: browser)").matches?"WEB_DISPLAY_MODE_BROWSER":"WEB_DISPLAY_MODE_UNKNOWN"}catch(a){return"WEB_DISPLAY_MODE_UNKNOWN"}}
;function fm(){this.df=!0}
function gm(){fm.h||(fm.h=new fm);return fm.h}
function hm(a,b){a={};var c=[];"SESSION_ID"in al&&c.push({key:"u",value:T("SESSION_ID")});if(c=oh(c))a.Authorization=c,c=b=null==b?void 0:b.sessionIndex,void 0===c&&(c=Number(T("SESSION_INDEX",0)),c=isNaN(c)?0:c),U("voice_search_auth_header_removal")||(a["X-Goog-AuthUser"]=c.toString()),"INNERTUBE_HOST_OVERRIDE"in al||(a["X-Origin"]=window.location.origin),void 0===b&&"DELEGATED_SESSION_ID"in al&&(a["X-Goog-PageId"]=T("DELEGATED_SESSION_ID"));return a}
;var im={identityType:"UNAUTHENTICATED_IDENTITY_TYPE_UNKNOWN"};function jm(a,b,c,d,e){kh.set(""+a,b,{Ob:c,path:"/",domain:void 0===d?"youtube.com":d,secure:void 0===e?!1:e})}
function km(a){return kh.get(""+a,void 0)}
function lm(a,b,c){kh.remove(""+a,void 0===b?"/":b,void 0===c?"youtube.com":c)}
function mm(){if(U("embeds_web_enable_cookie_detection_fix")){if(!B.navigator.cookieEnabled)return!1}else if(!kh.isEnabled())return!1;if(kh.h.cookie)return!0;U("embeds_web_enable_cookie_detection_fix")?kh.set("TESTCOOKIESENABLED","1",{Ob:60,Me:"none",secure:!0}):kh.set("TESTCOOKIESENABLED","1",{Ob:60});if("1"!==kh.get("TESTCOOKIESENABLED"))return!1;kh.remove("TESTCOOKIESENABLED");return!0}
;var nm=E("ytglobal.prefsUserPrefsPrefs_")||{};D("ytglobal.prefsUserPrefsPrefs_",nm);function om(){this.h=T("ALT_PREF_COOKIE_NAME","PREF");this.i=T("ALT_PREF_COOKIE_DOMAIN","youtube.com");var a=km(this.h);a&&this.parse(a)}
var pm;function qm(){pm||(pm=new om);return pm}
m=om.prototype;m.get=function(a,b){rm(a);sm(a);a=void 0!==nm[a]?nm[a].toString():null;return null!=a?a:b?b:""};
m.set=function(a,b){rm(a);sm(a);if(null==b)throw Error("ExpectedNotNull");nm[a]=b.toString()};
function tm(a){return!!((um("f"+(Math.floor(a/31)+1))||0)&1<<a%31)}
m.remove=function(a){rm(a);sm(a);delete nm[a]};
m.clear=function(){for(var a in nm)delete nm[a]};
function sm(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function rm(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function um(a){a=void 0!==nm[a]?nm[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
m.parse=function(a){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(nm[d]=c.toString())}};var wm={bluetooth:"CONN_DISCO",cellular:"CONN_CELLULAR_UNKNOWN",ethernet:"CONN_WIFI",none:"CONN_NONE",wifi:"CONN_WIFI",wimax:"CONN_CELLULAR_4G",other:"CONN_UNKNOWN",unknown:"CONN_UNKNOWN","slow-2g":"CONN_CELLULAR_2G","2g":"CONN_CELLULAR_2G","3g":"CONN_CELLULAR_3G","4g":"CONN_CELLULAR_4G"},xm={"slow-2g":"EFFECTIVE_CONNECTION_TYPE_SLOW_2G","2g":"EFFECTIVE_CONNECTION_TYPE_2G","3g":"EFFECTIVE_CONNECTION_TYPE_3G","4g":"EFFECTIVE_CONNECTION_TYPE_4G"};
function ym(){var a=B.navigator;return a?a.connection:void 0}
function zm(){var a=ym();if(a){var b=wm[a.type||"unknown"]||"CONN_UNKNOWN";a=wm[a.effectiveType||"unknown"]||"CONN_UNKNOWN";"CONN_CELLULAR_UNKNOWN"===b&&"CONN_UNKNOWN"!==a&&(b=a);if("CONN_UNKNOWN"!==b)return b;if("CONN_UNKNOWN"!==a)return a}}
function Am(){var a=ym();if(null!=a&&a.effectiveType)return xm.hasOwnProperty(a.effectiveType)?xm[a.effectiveType]:"EFFECTIVE_CONNECTION_TYPE_UNKNOWN"}
;function V(a){var b=A.apply(1,arguments);var c=Error.call(this,a);this.message=c.message;"stack"in c&&(this.stack=c.stack);this.args=[].concat(la(b))}
y(V,Error);function Bm(){try{return Cm(),!0}catch(a){return!1}}
function Cm(a){if(void 0!==T("DATASYNC_ID"))return T("DATASYNC_ID");throw new V("Datasync ID not set",void 0===a?"unknown":a);}
;function Dm(){}
function Em(a,b){return Pi.ab(a,0,b)}
Dm.prototype.pa=function(a,b){return this.ab(a,1,b)};
Dm.prototype.Db=function(a){var b=E("yt.scheduler.instance.addImmediateJob");b?b(a):a()};var Fm=Al("web_emulated_idle_callback_delay",300),Gm=1E3/60-3,Hm=[8,5,4,3,2,1,0];
function Im(a){a=void 0===a?{}:a;G.call(this);this.i=[];this.j={};this.da=this.h=0;this.ba=this.m=!1;this.K=[];this.W=this.ga=!1;for(var b=x(Hm),c=b.next();!c.done;c=b.next())this.i[c.value]=[];this.l=0;this.vc=a.timeout||1;this.F=Gm;this.A=0;this.xa=this.Be.bind(this);this.uc=this.gf.bind(this);this.Za=this.Md.bind(this);this.Cb=this.je.bind(this);this.Ub=this.Ee.bind(this);this.Ga=!!window.requestIdleCallback&&!!window.cancelIdleCallback&&!U("disable_scheduler_requestIdleCallback");(this.ja=!1!==
a.useRaf&&!!window.requestAnimationFrame)&&document.addEventListener("visibilitychange",this.xa)}
y(Im,G);m=Im.prototype;m.Db=function(a){var b=Za();Jm(this,a);a=Za()-b;this.m||(this.F-=a)};
m.ab=function(a,b,c){++this.da;if(10===b)return this.Db(a),this.da;var d=this.da;this.j[d]=a;this.m&&!c?this.K.push({id:d,priority:b}):(this.i[b].push(d),this.ba||this.m||(0!==this.h&&Km(this)!==this.A&&this.stop(),this.start()));return d};
m.qa=function(a){delete this.j[a]};
function Lm(a){a.K.length=0;for(var b=5;0<=b;b--)a.i[b].length=0;a.i[8].length=0;a.j={};a.stop()}
m.isHidden=function(){return!!document.hidden||!1};
function Mm(a){return!a.isHidden()&&a.ja}
function Km(a){if(a.i[8].length){if(a.W)return 4;if(Mm(a))return 3}for(var b=5;b>=a.l;b--)if(0<a.i[b].length)return 0<b?Mm(a)?3:2:1;return 0}
m.Ha=function(a){var b=E("yt.logging.errors.log");b&&b(a)};
function Jm(a,b){try{b()}catch(c){a.Ha(c)}}
function Nm(a){for(var b=x(Hm),c=b.next();!c.done;c=b.next())if(a.i[c.value].length)return!0;return!1}
m.je=function(a){var b=void 0;a&&(b=a.timeRemaining());this.ga=!0;Om(this,b);this.ga=!1};
m.gf=function(){Om(this)};
m.Md=function(){Pm(this)};
m.Ee=function(a){this.W=!0;var b=Km(this);4===b&&b!==this.A&&(this.stop(),this.start());Om(this,void 0,a);this.W=!1};
m.Be=function(){this.isHidden()||Pm(this);this.h&&(this.stop(),this.start())};
function Pm(a){a.stop();a.m=!0;for(var b=Za(),c=a.i[8];c.length;){var d=c.shift(),e=a.j[d];delete a.j[d];e&&Jm(a,e)}Qm(a);a.m=!1;Nm(a)&&a.start();b=Za()-b;a.F-=b}
function Qm(a){for(var b=0,c=a.K.length;b<c;b++){var d=a.K[b];a.i[d.priority].push(d.id)}a.K.length=0}
function Om(a,b,c){a.W&&4===a.A&&a.h||a.stop();a.m=!0;b=Za()+(b||a.F);for(var d=a.i[5];d.length;){var e=d.shift(),f=a.j[e];delete a.j[e];if(f){e=a;try{f(c)}catch(l){e.Ha(l)}}}for(d=a.i[4];d.length;)c=d.shift(),f=a.j[c],delete a.j[c],f&&Jm(a,f);d=a.ga?0:1;d=a.l>d?a.l:d;if(!(Za()>=b)){do{a:{c=a;f=d;for(e=3;e>=f;e--)for(var g=c.i[e];g.length;){var h=g.shift(),k=c.j[h];delete c.j[h];if(k){c=k;break a}}c=null}c&&Jm(a,c)}while(c&&Za()<b)}a.m=!1;Qm(a);a.F=Gm;Nm(a)&&a.start()}
m.start=function(){this.ba=!1;if(0===this.h)switch(this.A=Km(this),this.A){case 1:var a=this.Cb;this.h=this.Ga?window.requestIdleCallback(a,{timeout:3E3}):window.setTimeout(a,Fm);break;case 2:this.h=window.setTimeout(this.uc,this.vc);break;case 3:this.h=window.requestAnimationFrame(this.Ub);break;case 4:this.h=window.setTimeout(this.Za,0)}};
m.pause=function(){this.stop();this.ba=!0};
m.stop=function(){if(this.h){switch(this.A){case 1:var a=this.h;this.Ga?window.cancelIdleCallback(a):window.clearTimeout(a);break;case 2:case 4:window.clearTimeout(this.h);break;case 3:window.cancelAnimationFrame(this.h)}this.h=0}};
m.U=function(){Lm(this);this.stop();this.ja&&document.removeEventListener("visibilitychange",this.xa);G.prototype.U.call(this)};var Rm=E("yt.scheduler.instance.timerIdMap_")||{},Sm=Al("kevlar_tuner_scheduler_soft_state_timer_ms",800),Tm=0,Um=0;function Vm(){var a=E("ytglobal.schedulerInstanceInstance_");if(!a||a.V)a=new Im(T("scheduler")||{}),D("ytglobal.schedulerInstanceInstance_",a);return a}
function Wm(){Xm();var a=E("ytglobal.schedulerInstanceInstance_");a&&(Cc(a),D("ytglobal.schedulerInstanceInstance_",null))}
function Xm(){Lm(Vm());for(var a in Rm)Rm.hasOwnProperty(a)&&delete Rm[Number(a)]}
function Ym(a,b,c){if(!c)return c=void 0===c,-Vm().ab(a,b,c);var d=window.setTimeout(function(){var e=Vm().ab(a,b);Rm[d]=e},c);
return d}
function Zm(a){Vm().Db(a)}
function $m(a){var b=Vm();if(0>a)b.qa(-a);else{var c=Rm[a];c?(b.qa(c),delete Rm[a]):window.clearTimeout(a)}}
function an(){bn()}
function bn(){window.clearTimeout(Tm);Vm().start()}
function cn(){Vm().pause();window.clearTimeout(Tm);Tm=window.setTimeout(an,Sm)}
function dn(){window.clearTimeout(Um);Um=window.setTimeout(function(){en(0)},Sm)}
function en(a){dn();var b=Vm();b.l=a;b.start()}
function fn(a){dn();var b=Vm();b.l>a&&(b.l=a,b.start())}
function gn(){window.clearTimeout(Um);var a=Vm();a.l=0;a.start()}
;function hn(){Dm.apply(this,arguments)}
y(hn,Dm);function jn(){hn.h||(hn.h=new hn);return hn.h}
hn.prototype.ab=function(a,b,c){void 0!==c&&Number.isNaN(Number(c))&&(c=void 0);var d=E("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):xl(a,c||0)};
hn.prototype.qa=function(a){if(void 0===a||!Number.isNaN(Number(a))){var b=E("yt.scheduler.instance.cancelJob");b?b(a):window.clearTimeout(a)}};
hn.prototype.start=function(){var a=E("yt.scheduler.instance.start");a&&a()};
hn.prototype.pause=function(){var a=E("yt.scheduler.instance.pause");a&&a()};
var Pi=jn();
U("web_scheduler_auto_init")&&!E("yt.scheduler.initialized")&&(D("yt.scheduler.instance.dispose",Wm),D("yt.scheduler.instance.addJob",Ym),D("yt.scheduler.instance.addImmediateJob",Zm),D("yt.scheduler.instance.cancelJob",$m),D("yt.scheduler.instance.cancelAllJobs",Xm),D("yt.scheduler.instance.start",bn),D("yt.scheduler.instance.pause",cn),D("yt.scheduler.instance.setPriorityThreshold",en),D("yt.scheduler.instance.enablePriorityThreshold",fn),D("yt.scheduler.instance.clearPriorityThreshold",gn),D("yt.scheduler.initialized",
!0));function kn(a){var b=new oj;this.h=(a=b.isAvailable()?a?new pj(b,a):b:null)?new jj(a):null;this.i=document.domain||window.location.hostname}
kn.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.h)try{this.h.set(a,b,Date.now()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape((new $h).serialize(b))}catch(f){return}else e=escape(b);jm(a,e,c,this.i)};
kn.prototype.get=function(a,b){var c=void 0,d=!this.h;if(!d)try{c=this.h.get(a)}catch(e){d=!0}if(d&&(c=km(a))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
kn.prototype.remove=function(a){this.h&&this.h.remove(a);lm(a,"/",this.i)};var ln=function(){var a;return function(){a||(a=new kn("ytidb"));return a}}();
function mn(){var a;return null==(a=ln())?void 0:a.get("LAST_RESULT_ENTRY_KEY",!0)}
;var nn=[],on,pn=!1;function qn(){var a={};for(on=new rn(void 0===a.handleError?sn:a.handleError,void 0===a.logEvent?tn:a.logEvent);0<nn.length;)switch(a=nn.shift(),a.type){case "ERROR":on.Ha(a.payload);break;case "EVENT":on.logEvent(a.eventType,a.payload)}}
function un(a){pn||(on?on.Ha(a):(nn.push({type:"ERROR",payload:a}),10<nn.length&&nn.shift()))}
function vn(a,b){pn||(on?on.logEvent(a,b):(nn.push({type:"EVENT",eventType:a,payload:b}),10<nn.length&&nn.shift()))}
;function wn(a){if(0<=a.indexOf(":"))throw Error("Database name cannot contain ':'");}
function xn(a){return a.substr(0,a.indexOf(":"))||a}
;var yn=De||Ee;function zn(a){var b=Jc();return b?0<=b.toLowerCase().indexOf(a):!1}
;var An={},Bn=(An.AUTH_INVALID="No user identifier specified.",An.EXPLICIT_ABORT="Transaction was explicitly aborted.",An.IDB_NOT_SUPPORTED="IndexedDB is not supported.",An.MISSING_INDEX="Index not created.",An.MISSING_OBJECT_STORES="Object stores not created.",An.DB_DELETED_BY_MISSING_OBJECT_STORES="Database is deleted because expected object stores were not created.",An.DB_REOPENED_BY_MISSING_OBJECT_STORES="Database is reopened because expected object stores were not created.",An.UNKNOWN_ABORT="Transaction was aborted for unknown reasons.",
An.QUOTA_EXCEEDED="The current transaction exceeded its quota limitations.",An.QUOTA_MAYBE_EXCEEDED="The current transaction may have failed because of exceeding quota limitations.",An.EXECUTE_TRANSACTION_ON_CLOSED_DB="Can't start a transaction on a closed database",An.INCOMPATIBLE_DB_VERSION="The binary is incompatible with the database version",An),Cn={},Dn=(Cn.AUTH_INVALID="ERROR",Cn.EXECUTE_TRANSACTION_ON_CLOSED_DB="WARNING",Cn.EXPLICIT_ABORT="IGNORED",Cn.IDB_NOT_SUPPORTED="ERROR",Cn.MISSING_INDEX=
"WARNING",Cn.MISSING_OBJECT_STORES="ERROR",Cn.DB_DELETED_BY_MISSING_OBJECT_STORES="WARNING",Cn.DB_REOPENED_BY_MISSING_OBJECT_STORES="WARNING",Cn.QUOTA_EXCEEDED="WARNING",Cn.QUOTA_MAYBE_EXCEEDED="WARNING",Cn.UNKNOWN_ABORT="WARNING",Cn.INCOMPATIBLE_DB_VERSION="WARNING",Cn),En={},Fn=(En.AUTH_INVALID=!1,En.EXECUTE_TRANSACTION_ON_CLOSED_DB=!1,En.EXPLICIT_ABORT=!1,En.IDB_NOT_SUPPORTED=!1,En.MISSING_INDEX=!1,En.MISSING_OBJECT_STORES=!1,En.DB_DELETED_BY_MISSING_OBJECT_STORES=!1,En.DB_REOPENED_BY_MISSING_OBJECT_STORES=
!1,En.QUOTA_EXCEEDED=!1,En.QUOTA_MAYBE_EXCEEDED=!0,En.UNKNOWN_ABORT=!0,En.INCOMPATIBLE_DB_VERSION=!1,En);function Gn(a,b,c,d,e){b=void 0===b?{}:b;c=void 0===c?Bn[a]:c;d=void 0===d?Dn[a]:d;e=void 0===e?Fn[a]:e;V.call(this,c,Object.assign({},{name:"YtIdbKnownError",isSw:void 0===self.document,isIframe:self!==self.top,type:a},b));this.type=a;this.message=c;this.level=d;this.h=e;Object.setPrototypeOf(this,Gn.prototype)}
y(Gn,V);function Hn(a,b){Gn.call(this,"MISSING_OBJECT_STORES",{expectedObjectStores:b,foundObjectStores:a},Bn.MISSING_OBJECT_STORES);Object.setPrototypeOf(this,Hn.prototype)}
y(Hn,Gn);function In(a,b){var c=Error.call(this);this.message=c.message;"stack"in c&&(this.stack=c.stack);this.index=a;this.objectStore=b;Object.setPrototypeOf(this,In.prototype)}
y(In,Error);var Jn=["The database connection is closing","Can't start a transaction on a closed database","A mutation operation was attempted on a database that did not allow mutations"];
function Kn(a,b,c,d){b=xn(b);var e=a instanceof Error?a:Error("Unexpected error: "+a);if(e instanceof Gn)return e;a={objectStoreNames:c,dbName:b,dbVersion:d};if("QuotaExceededError"===e.name)return new Gn("QUOTA_EXCEEDED",a);if(Fe&&"UnknownError"===e.name)return new Gn("QUOTA_MAYBE_EXCEEDED",a);if(e instanceof In)return new Gn("MISSING_INDEX",Object.assign({},a,{objectStore:e.objectStore,index:e.index}));if("InvalidStateError"===e.name&&Jn.some(function(f){return e.message.includes(f)}))return new Gn("EXECUTE_TRANSACTION_ON_CLOSED_DB",
a);
if("AbortError"===e.name)return new Gn("UNKNOWN_ABORT",a,e.message);e.args=[Object.assign({},a,{name:"IdbError",od:e.name})];e.level="WARNING";return e}
function Ln(a,b,c){var d=mn();return new Gn("IDB_NOT_SUPPORTED",{context:{caller:a,publicName:b,version:c,hasSucceededOnce:null==d?void 0:d.hasSucceededOnce}})}
;function Mn(a){if(!a)throw Error();throw a;}
function Nn(a){return a}
function On(a){this.h=a}
function Pn(a){function b(e){if("PENDING"===d.state.status){d.state={status:"REJECTED",reason:e};e=x(d.i);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
function c(e){if("PENDING"===d.state.status){d.state={status:"FULFILLED",value:e};e=x(d.h);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
var d=this;this.state={status:"PENDING"};this.h=[];this.i=[];a=a.h;try{a(c,b)}catch(e){b(e)}}
Pn.all=function(a){return new Pn(new On(function(b,c){var d=[],e=a.length;0===e&&b(d);for(var f={rb:0};f.rb<a.length;f={rb:f.rb},++f.rb)Pn.resolve(a[f.rb]).then(function(g){return function(h){d[g.rb]=h;e--;0===e&&b(d)}}(f)).catch(function(g){c(g)})}))};
Pn.resolve=function(a){return new Pn(new On(function(b,c){a instanceof Pn?a.then(b,c):b(a)}))};
Pn.reject=function(a){return new Pn(new On(function(b,c){c(a)}))};
Pn.prototype.then=function(a,b){var c=this,d=null!=a?a:Nn,e=null!=b?b:Mn;return new Pn(new On(function(f,g){"PENDING"===c.state.status?(c.h.push(function(){Qn(c,c,d,f,g)}),c.i.push(function(){Rn(c,c,e,f,g)})):"FULFILLED"===c.state.status?Qn(c,c,d,f,g):"REJECTED"===c.state.status&&Rn(c,c,e,f,g)}))};
Pn.prototype.catch=function(a){return this.then(void 0,a)};
function Qn(a,b,c,d,e){try{if("FULFILLED"!==a.state.status)throw Error("calling handleResolve before the promise is fulfilled.");var f=c(a.state.value);f instanceof Pn?Sn(a,b,f,d,e):d(f)}catch(g){e(g)}}
function Rn(a,b,c,d,e){try{if("REJECTED"!==a.state.status)throw Error("calling handleReject before the promise is rejected.");var f=c(a.state.reason);f instanceof Pn?Sn(a,b,f,d,e):d(f)}catch(g){e(g)}}
function Sn(a,b,c,d,e){b===c?e(new TypeError("Circular promise chain detected.")):c.then(function(f){f instanceof Pn?Sn(a,b,f,d,e):d(f)},function(f){e(f)})}
;function Tn(a,b,c){function d(){c(a.error);f()}
function e(){b(a.result);f()}
function f(){try{a.removeEventListener("success",e),a.removeEventListener("error",d)}catch(g){}}
a.addEventListener("success",e);a.addEventListener("error",d)}
function Un(a){return new Promise(function(b,c){Tn(a,b,c)})}
function Vn(a){return new Pn(new On(function(b,c){Tn(a,b,c)}))}
;function Wn(a,b){return new Pn(new On(function(c,d){function e(){var f=a?b(a):null;f?f.then(function(g){a=g;e()},d):c()}
e()}))}
;var Xn=window,W=Xn.ytcsi&&Xn.ytcsi.now?Xn.ytcsi.now:Xn.performance&&Xn.performance.timing&&Xn.performance.now&&Xn.performance.timing.navigationStart?function(){return Xn.performance.timing.navigationStart+Xn.performance.now()}:function(){return(new Date).getTime()};function Yn(a,b){this.h=a;this.options=b;this.transactionCount=0;this.j=Math.round(W());this.i=!1}
m=Yn.prototype;m.add=function(a,b,c){return Zn(this,[a],{mode:"readwrite",la:!0},function(d){return d.objectStore(a).add(b,c)})};
m.clear=function(a){return Zn(this,[a],{mode:"readwrite",la:!0},function(b){return b.objectStore(a).clear()})};
m.close=function(){this.h.close();var a;(null==(a=this.options)?0:a.closed)&&this.options.closed()};
m.count=function(a,b){return Zn(this,[a],{mode:"readonly",la:!0},function(c){return c.objectStore(a).count(b)})};
function $n(a,b,c){a=a.h.createObjectStore(b,c);return new ao(a)}
m.delete=function(a,b){return Zn(this,[a],{mode:"readwrite",la:!0},function(c){return c.objectStore(a).delete(b)})};
m.get=function(a,b){return Zn(this,[a],{mode:"readonly",la:!0},function(c){return c.objectStore(a).get(b)})};
function bo(a,b,c){return Zn(a,[b],{mode:"readwrite",la:!0},function(d){d=d.objectStore(b);return Vn(d.h.put(c,void 0))})}
m.objectStoreNames=function(){return Array.from(this.h.objectStoreNames)};
function Zn(a,b,c,d){var e,f,g,h,k,l,n,p,r,t,v,w;return z(function(C){switch(C.h){case 1:var F={mode:"readonly",la:!1,tag:"IDB_TRANSACTION_TAG_UNKNOWN"};"string"===typeof c?F.mode=c:Object.assign(F,c);e=F;a.transactionCount++;f=e.la?3:1;g=0;case 2:if(h){C.B(4);break}g++;k=Math.round(W());Aa(C,5);l=a.h.transaction(b,e.mode);F=C.yield;var K=new co(l);K=eo(K,d);return F.call(C,K,7);case 7:return n=C.i,p=Math.round(W()),fo(a,k,p,g,void 0,b.join(),e),C.return(n);case 5:r=Ba(C);t=Math.round(W());v=Kn(r,
a.h.name,b.join(),a.h.version);if((w=v instanceof Gn&&!v.h)||g>=f)fo(a,k,t,g,v,b.join(),e),h=v;C.B(2);break;case 4:return C.return(Promise.reject(h))}})}
function fo(a,b,c,d,e,f,g){b=c-b;e?(e instanceof Gn&&("QUOTA_EXCEEDED"===e.type||"QUOTA_MAYBE_EXCEEDED"===e.type)&&vn("QUOTA_EXCEEDED",{dbName:xn(a.h.name),objectStoreNames:f,transactionCount:a.transactionCount,transactionMode:g.mode}),e instanceof Gn&&"UNKNOWN_ABORT"===e.type&&(c-=a.j,0>c&&c>=Math.pow(2,31)&&(c=0),vn("TRANSACTION_UNEXPECTEDLY_ABORTED",{objectStoreNames:f,transactionDuration:b,transactionCount:a.transactionCount,dbDuration:c}),a.i=!0),go(a,!1,d,f,b,g.tag),un(e)):go(a,!0,d,f,b,g.tag)}
function go(a,b,c,d,e,f){vn("TRANSACTION_ENDED",{objectStoreNames:d,connectionHasUnknownAbortedTransaction:a.i,duration:e,isSuccessful:b,tryCount:c,tag:void 0===f?"IDB_TRANSACTION_TAG_UNKNOWN":f})}
m.getName=function(){return this.h.name};
function ao(a){this.h=a}
m=ao.prototype;m.add=function(a,b){return Vn(this.h.add(a,b))};
m.autoIncrement=function(){return this.h.autoIncrement};
m.clear=function(){return Vn(this.h.clear()).then(function(){})};
function ho(a,b,c){a.h.createIndex(b,c,{unique:!1})}
m.count=function(a){return Vn(this.h.count(a))};
function io(a,b){return jo(a,{query:b},function(c){return c.delete().then(function(){return ko(c)})}).then(function(){})}
m.delete=function(a){return a instanceof IDBKeyRange?io(this,a):Vn(this.h.delete(a))};
m.get=function(a){return Vn(this.h.get(a))};
m.index=function(a){try{return new lo(this.h.index(a))}catch(b){if(b instanceof Error&&"NotFoundError"===b.name)throw new In(a,this.h.name);throw b;}};
m.getName=function(){return this.h.name};
m.keyPath=function(){return this.h.keyPath};
function jo(a,b,c){a=a.h.openCursor(b.query,b.direction);return mo(a).then(function(d){return Wn(d,c)})}
function co(a){var b=this;this.h=a;this.i=new Map;this.aborted=!1;this.done=new Promise(function(c,d){b.h.addEventListener("complete",function(){c()});
b.h.addEventListener("error",function(e){e.currentTarget===e.target&&d(b.h.error)});
b.h.addEventListener("abort",function(){var e=b.h.error;if(e)d(e);else if(!b.aborted){e=Gn;for(var f=b.h.objectStoreNames,g=[],h=0;h<f.length;h++){var k=f.item(h);if(null===k)throw Error("Invariant: item in DOMStringList is null");g.push(k)}e=new e("UNKNOWN_ABORT",{objectStoreNames:g.join(),dbName:b.h.db.name,mode:b.h.mode});d(e)}})})}
function eo(a,b){var c=new Promise(function(d,e){try{b(a).then(function(f){d(f)}).catch(e)}catch(f){e(f),a.abort()}});
return Promise.all([c,a.done]).then(function(d){return x(d).next().value})}
co.prototype.abort=function(){this.h.abort();this.aborted=!0;throw new Gn("EXPLICIT_ABORT");};
co.prototype.objectStore=function(a){a=this.h.objectStore(a);var b=this.i.get(a);b||(b=new ao(a),this.i.set(a,b));return b};
function lo(a){this.h=a}
m=lo.prototype;m.count=function(a){return Vn(this.h.count(a))};
m.delete=function(a){return no(this,{query:a},function(b){return b.delete().then(function(){return ko(b)})})};
m.get=function(a){return Vn(this.h.get(a))};
m.keyPath=function(){return this.h.keyPath};
m.unique=function(){return this.h.unique};
function no(a,b,c){a=a.h.openCursor(void 0===b.query?null:b.query,void 0===b.direction?"next":b.direction);return mo(a).then(function(d){return Wn(d,c)})}
function oo(a,b){this.request=a;this.cursor=b}
function mo(a){return Vn(a).then(function(b){return b?new oo(a,b):null})}
function ko(a){a.cursor.continue(void 0);return mo(a.request)}
oo.prototype.delete=function(){return Vn(this.cursor.delete()).then(function(){})};
oo.prototype.getValue=function(){return this.cursor.value};
oo.prototype.update=function(a){return Vn(this.cursor.update(a))};function po(a,b,c){return new Promise(function(d,e){function f(){r||(r=new Yn(g.result,{closed:p}));return r}
var g=void 0!==b?self.indexedDB.open(a,b):self.indexedDB.open(a);var h=c.Od,k=c.blocking,l=c.ef,n=c.upgrade,p=c.closed,r;g.addEventListener("upgradeneeded",function(t){try{if(null===t.newVersion)throw Error("Invariant: newVersion on IDbVersionChangeEvent is null");if(null===g.transaction)throw Error("Invariant: transaction on IDbOpenDbRequest is null");t.dataLoss&&"none"!==t.dataLoss&&vn("IDB_DATA_CORRUPTED",{reason:t.dataLossMessage||"unknown reason",dbName:xn(a)});var v=f(),w=new co(g.transaction);
n&&n(v,function(C){return t.oldVersion<C&&t.newVersion>=C},w);
w.done.catch(function(C){e(C)})}catch(C){e(C)}});
g.addEventListener("success",function(){var t=g.result;k&&t.addEventListener("versionchange",function(){k(f())});
t.addEventListener("close",function(){vn("IDB_UNEXPECTEDLY_CLOSED",{dbName:xn(a),dbVersion:t.version});l&&l()});
d(f())});
g.addEventListener("error",function(){e(g.error)});
h&&g.addEventListener("blocked",function(){h()})})}
function qo(a,b,c){c=void 0===c?{}:c;return po(a,b,c)}
function ro(a,b){b=void 0===b?{}:b;var c,d,e,f;return z(function(g){if(1==g.h)return Aa(g,2),c=self.indexedDB.deleteDatabase(a),d=b,(e=d.Od)&&c.addEventListener("blocked",function(){e()}),g.yield(Un(c),4);
if(2!=g.h)g.h=0,g.l=0;else throw f=Ba(g),Kn(f,a,"",-1);})}
;function so(a,b){this.name=a;this.options=b;this.j=!0;this.v=this.l=0}
so.prototype.i=function(a,b,c){c=void 0===c?{}:c;return qo(a,b,c)};
so.prototype.delete=function(a){a=void 0===a?{}:a;return ro(this.name,a)};
function to(a,b){return new Gn("INCOMPATIBLE_DB_VERSION",{dbName:a.name,oldVersion:a.options.version,newVersion:b})}
function uo(a,b){if(!b)throw Ln("openWithToken",xn(a.name));return a.open()}
so.prototype.open=function(){function a(){var f,g,h,k,l,n,p,r,t,v;return z(function(w){switch(w.h){case 1:return g=null!=(f=Error().stack)?f:"",Aa(w,2),w.yield(c.i(c.name,c.options.version,e),4);case 4:for(var C=h=w.i,F=c.options,K=[],N=x(Object.keys(F.xb)),S=N.next();!S.done;S=N.next()){S=S.value;var da=F.xb[S],ta=void 0===da.He?Number.MAX_VALUE:da.He;!(C.h.version>=da.Fb)||C.h.version>=ta||C.h.objectStoreNames.contains(S)||K.push(S)}k=K;if(0===k.length){w.B(5);break}l=Object.keys(c.options.xb);
n=h.objectStoreNames();if(c.v<Al("ytidb_reopen_db_retries",0))return c.v++,h.close(),un(new Gn("DB_REOPENED_BY_MISSING_OBJECT_STORES",{dbName:c.name,expectedObjectStores:l,foundObjectStores:n})),w.return(a());if(!(c.l<Al("ytidb_remake_db_retries",1))){w.B(6);break}c.l++;return w.yield(c.delete(),7);case 7:return un(new Gn("DB_DELETED_BY_MISSING_OBJECT_STORES",{dbName:c.name,expectedObjectStores:l,foundObjectStores:n})),w.return(a());case 6:throw new Hn(n,l);case 5:return w.return(h);case 2:p=Ba(w);
if(p instanceof DOMException?"VersionError"!==p.name:"DOMError"in self&&p instanceof DOMError?"VersionError"!==p.name:!(p instanceof Object&&"message"in p)||"An attempt was made to open a database using a lower version than the existing version."!==p.message){w.B(8);break}return w.yield(c.i(c.name,void 0,Object.assign({},e,{upgrade:void 0})),9);case 9:r=w.i;t=r.h.version;if(void 0!==c.options.version&&t>c.options.version+1)throw r.close(),c.j=!1,to(c,t);return w.return(r);case 8:throw b(),p instanceof
Error&&!U("ytidb_async_stack_killswitch")&&(p.stack=p.stack+"\n"+g.substring(g.indexOf("\n")+1)),Kn(p,c.name,"",null!=(v=c.options.version)?v:-1);}})}
function b(){c.h===d&&(c.h=void 0)}
var c=this;if(!this.j)throw to(this);if(this.h)return this.h;var d,e={blocking:function(f){f.close()},
closed:b,ef:b,upgrade:this.options.upgrade};return this.h=d=a()};var vo=new so("YtIdbMeta",{xb:{databases:{Fb:1}},upgrade:function(a,b){b(1)&&$n(a,"databases",{keyPath:"actualName"})}});
function wo(a,b){var c;return z(function(d){if(1==d.h)return d.yield(uo(vo,b),2);c=d.i;return d.return(Zn(c,["databases"],{la:!0,mode:"readwrite"},function(e){var f=e.objectStore("databases");return f.get(a.actualName).then(function(g){if(g?a.actualName!==g.actualName||a.publicName!==g.publicName||a.userIdentifier!==g.userIdentifier:1)return Vn(f.h.put(a,void 0)).then(function(){})})}))})}
function xo(a,b){var c;return z(function(d){if(1==d.h)return a?d.yield(uo(vo,b),2):d.return();c=d.i;return d.return(c.delete("databases",a))})}
function yo(a,b){var c,d;return z(function(e){return 1==e.h?(c=[],e.yield(uo(vo,b),2)):3!=e.h?(d=e.i,e.yield(Zn(d,["databases"],{la:!0,mode:"readonly"},function(f){c.length=0;return jo(f.objectStore("databases"),{},function(g){a(g.getValue())&&c.push(g.getValue());return ko(g)})}),3)):e.return(c)})}
function zo(a){return yo(function(b){return"LogsDatabaseV2"===b.publicName&&void 0!==b.userIdentifier},a)}
function Ao(a,b,c){return yo(function(d){return c?void 0!==d.userIdentifier&&!a.includes(d.userIdentifier)&&c.includes(d.publicName):void 0!==d.userIdentifier&&!a.includes(d.userIdentifier)},b)}
function Bo(a){var b,c;return z(function(d){if(1==d.h)return b=Cm("YtIdbMeta hasAnyMeta other"),d.yield(yo(function(e){return void 0!==e.userIdentifier&&e.userIdentifier!==b},a),2);
c=d.i;return d.return(0<c.length)})}
;var Co,Do=new function(){}(new function(){});
function Eo(){var a,b,c,d;return z(function(e){switch(e.h){case 1:a=mn();if(null==(b=a)?0:b.hasSucceededOnce)return e.return(!0);var f;if(f=yn)f=/WebKit\/([0-9]+)/.exec(Jc()),f=!!(f&&600<=parseInt(f[1],10));f&&(f=/WebKit\/([0-9]+)/.exec(Jc()),f=!(f&&602<=parseInt(f[1],10)));if(f||Wc)return e.return(!1);try{if(c=self,!(c.indexedDB&&c.IDBIndex&&c.IDBKeyRange&&c.IDBObjectStore))return e.return(!1)}catch(g){return e.return(!1)}if(!("IDBTransaction"in self&&"objectStoreNames"in IDBTransaction.prototype))return e.return(!1);
Aa(e,2);d={actualName:"yt-idb-test-do-not-use",publicName:"yt-idb-test-do-not-use",userIdentifier:void 0};return e.yield(wo(d,Do),4);case 4:return e.yield(xo("yt-idb-test-do-not-use",Do),5);case 5:return e.return(!0);case 2:return Ba(e),e.return(!1)}})}
function Fo(){if(void 0!==Co)return Co;pn=!0;return Co=Eo().then(function(a){pn=!1;var b;if(null!=(b=ln())&&b.h){var c;b={hasSucceededOnce:(null==(c=mn())?void 0:c.hasSucceededOnce)||a};var d;null==(d=ln())||d.set("LAST_RESULT_ENTRY_KEY",b,2592E3,!0)}return a})}
function Go(){return E("ytglobal.idbToken_")||void 0}
function Ho(){var a=Go();return a?Promise.resolve(a):Fo().then(function(b){(b=b?Do:void 0)&&D("ytglobal.idbToken_",b);return b})}
;var Io=0;function Jo(a,b){Io||(Io=Pi.pa(function(){var c,d,e,f,g;return z(function(h){switch(h.h){case 1:return h.yield(Ho(),2);case 2:c=h.i;if(!c)return h.return();d=!0;Aa(h,3);return h.yield(Ao(a,c,b),5);case 5:e=h.i;if(!e.length){d=!1;h.B(6);break}f=e[0];return h.yield(ro(f.actualName),7);case 7:return h.yield(xo(f.actualName,c),6);case 6:h.h=4;h.l=0;break;case 3:g=Ba(h),un(g),d=!1;case 4:Pi.qa(Io),Io=0,d&&Jo(a,b),h.h=0}})}))}
function Ko(){var a;return z(function(b){return 1==b.h?b.yield(Ho(),2):(a=b.i)?b.return(Bo(a)):b.return(!1)})}
new yi;function Lo(a){if(!Bm())throw a=new Gn("AUTH_INVALID",{dbName:a}),un(a),a;var b=Cm();return{actualName:a+":"+b,publicName:a,userIdentifier:b}}
function Mo(a,b,c,d){var e,f,g,h,k,l;return z(function(n){switch(n.h){case 1:return f=null!=(e=Error().stack)?e:"",n.yield(Ho(),2);case 2:g=n.i;if(!g)throw h=Ln("openDbImpl",a,b),U("ytidb_async_stack_killswitch")||(h.stack=h.stack+"\n"+f.substring(f.indexOf("\n")+1)),un(h),h;wn(a);k=c?{actualName:a,publicName:a,userIdentifier:void 0}:Lo(a);Aa(n,3);return n.yield(wo(k,g),5);case 5:return n.yield(qo(k.actualName,b,d),6);case 6:return n.return(n.i);case 3:return l=Ba(n),Aa(n,7),n.yield(xo(k.actualName,
g),9);case 9:n.h=8;n.l=0;break;case 7:Ba(n);case 8:throw l;}})}
function No(a,b,c){c=void 0===c?{}:c;return Mo(a,b,!1,c)}
function Oo(a,b,c){c=void 0===c?{}:c;return Mo(a,b,!0,c)}
function Po(a,b){b=void 0===b?{}:b;var c,d;return z(function(e){if(1==e.h)return e.yield(Ho(),2);if(3!=e.h){c=e.i;if(!c)return e.return();wn(a);d=Lo(a);return e.yield(ro(d.actualName,b),3)}return e.yield(xo(d.actualName,c),0)})}
function Qo(a,b,c){a=a.map(function(d){return z(function(e){return 1==e.h?e.yield(ro(d.actualName,b),2):e.yield(xo(d.actualName,c),0)})});
return Promise.all(a).then(function(){})}
function Ro(){var a=void 0===a?{}:a;var b,c;return z(function(d){if(1==d.h)return d.yield(Ho(),2);if(3!=d.h){b=d.i;if(!b)return d.return();wn("LogsDatabaseV2");return d.yield(zo(b),3)}c=d.i;return d.yield(Qo(c,a,b),0)})}
function So(a,b){b=void 0===b?{}:b;var c;return z(function(d){if(1==d.h)return d.yield(Ho(),2);if(3!=d.h){c=d.i;if(!c)return d.return();wn(a);return d.yield(ro(a,b),3)}return d.yield(xo(a,c),0)})}
;function To(a,b){so.call(this,a,b);this.options=b;wn(a)}
y(To,so);function Uo(a,b){var c;return function(){c||(c=new To(a,b));return c}}
To.prototype.i=function(a,b,c){c=void 0===c?{}:c;return(this.options.shared?Oo:No)(a,b,Object.assign({},c))};
To.prototype.delete=function(a){a=void 0===a?{}:a;return(this.options.shared?So:Po)(this.name,a)};
function Vo(a,b){return Uo(a,b)}
;var Wo={},Xo=Vo("ytGcfConfig",{xb:(Wo.coldConfigStore={Fb:1},Wo.hotConfigStore={Fb:1},Wo),shared:!1,upgrade:function(a,b){b(1)&&(ho($n(a,"hotConfigStore",{keyPath:"key",autoIncrement:!0}),"hotTimestampIndex","timestamp"),ho($n(a,"coldConfigStore",{keyPath:"key",autoIncrement:!0}),"coldTimestampIndex","timestamp"))},
version:1});function Yo(a){return uo(Xo(),a)}
function Zo(a,b,c){var d,e,f;return z(function(g){switch(g.h){case 1:return d={config:a,hashData:b,timestamp:W()},g.yield(Yo(c),2);case 2:return e=g.i,g.yield(e.clear("hotConfigStore"),3);case 3:return g.yield(bo(e,"hotConfigStore",d),4);case 4:return f=g.i,g.return(f)}})}
function $o(a,b,c,d){var e,f,g;return z(function(h){switch(h.h){case 1:return e={config:a,hashData:b,configData:c,timestamp:W()},h.yield(Yo(d),2);case 2:return f=h.i,h.yield(f.clear("coldConfigStore"),3);case 3:return h.yield(bo(f,"coldConfigStore",e),4);case 4:return g=h.i,h.return(g)}})}
function ap(a){var b,c;return z(function(d){return 1==d.h?d.yield(Yo(a),2):3!=d.h?(b=d.i,c=void 0,d.yield(Zn(b,["coldConfigStore"],{mode:"readwrite",la:!0},function(e){return no(e.objectStore("coldConfigStore").index("coldTimestampIndex"),{direction:"prev"},function(f){c=f.getValue()})}),3)):d.return(c)})}
function bp(a){var b,c;return z(function(d){return 1==d.h?d.yield(Yo(a),2):3!=d.h?(b=d.i,c=void 0,d.yield(Zn(b,["hotConfigStore"],{mode:"readwrite",la:!0},function(e){return no(e.objectStore("hotConfigStore").index("hotTimestampIndex"),{direction:"prev"},function(f){c=f.getValue()})}),3)):d.return(c)})}
;function cp(){G.call(this);this.i=[];this.h=[];var a=E("yt.gcf.config.hotUpdateCallbacks");a?(this.i=[].concat(la(a)),this.h=a):(this.h=[],D("yt.gcf.config.hotUpdateCallbacks",this.h))}
y(cp,G);cp.prototype.U=function(){for(var a=x(this.i),b=a.next();!b.done;b=a.next()){var c=this.h;b=c.indexOf(b.value);0<=b&&c.splice(b,1)}this.i.length=0;G.prototype.U.call(this)};function dp(){this.h=0;this.i=new cp}
function ep(){var a;return null!=(a=E("yt.gcf.config.hotConfigGroup"))?a:T("RAW_HOT_CONFIG_GROUP")}
function fp(a,b,c){var d,e,f;return z(function(g){switch(g.h){case 1:if(!U("start_client_gcf")){g.B(0);break}c&&(a.j=c,D("yt.gcf.config.hotConfigGroup",a.j||null));a.l(b);d=Go();if(!d){g.B(3);break}if(c){g.B(4);break}return g.yield(bp(d),5);case 5:e=g.i,c=null==(f=e)?void 0:f.config;case 4:return g.yield(Zo(c,b,d),3);case 3:if(c)for(var h=c,k=x(a.i.h),l=k.next();!l.done;l=k.next())l=l.value,l(h);g.h=0}})}
function gp(a,b,c){var d,e,f,g;return z(function(h){if(1==h.h){if(!U("start_client_gcf"))return h.B(0);a.coldHashData=b;D("yt.gcf.config.coldHashData",a.coldHashData||null);return(d=Go())?c?h.B(4):h.yield(ap(d),5):h.B(0)}4!=h.h&&(e=h.i,c=null==(f=e)?void 0:f.config);if(!c)return h.B(0);g=c.configData;return h.yield($o(c,b,g,d),0)})}
function hp(){if(!dp.h){var a=new dp;dp.h=a}a=dp.h;var b=W()-a.h;if(!(0!==a.h&&b<Al("send_config_hash_timer"))){b=E("yt.gcf.config.coldConfigData");var c=E("yt.gcf.config.hotHashData"),d=E("yt.gcf.config.coldHashData");b&&c&&d&&(a.h=W());return{coldConfigData:b,hotHashData:c,coldHashData:d}}}
dp.prototype.l=function(a){this.hotHashData=a;D("yt.gcf.config.hotHashData",this.hotHashData||null)};function ip(){return"INNERTUBE_API_KEY"in al&&"INNERTUBE_API_VERSION"in al}
function jp(){return{innertubeApiKey:T("INNERTUBE_API_KEY"),innertubeApiVersion:T("INNERTUBE_API_VERSION"),ke:T("INNERTUBE_CONTEXT_CLIENT_CONFIG_INFO"),hd:T("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),Kg:T("INNERTUBE_CONTEXT_CLIENT_NAME",1),innertubeContextClientVersion:T("INNERTUBE_CONTEXT_CLIENT_VERSION"),me:T("INNERTUBE_CONTEXT_HL"),le:T("INNERTUBE_CONTEXT_GL"),ne:T("INNERTUBE_HOST_OVERRIDE")||"",pe:!!T("INNERTUBE_USE_THIRD_PARTY_AUTH",!1),oe:!!T("INNERTUBE_OMIT_API_KEY_WHEN_AUTH_HEADER_IS_PRESENT",
!1),appInstallData:T("SERIALIZED_CLIENT_CONFIG_DATA")}}
function kp(a){var b={client:{hl:a.me,gl:a.le,clientName:a.hd,clientVersion:a.innertubeContextClientVersion,configInfo:a.ke}};navigator.userAgent&&(b.client.userAgent=String(navigator.userAgent));var c=B.devicePixelRatio;c&&1!=c&&(b.client.screenDensityFloat=String(c));c=T("EXPERIMENTS_TOKEN","");""!==c&&(b.client.experimentsToken=c);c=Bl();0<c.length&&(b.request={internalExperimentFlags:c});c=a.hd;if(("WEB"===c||"MWEB"===c||1===c||2===c)&&b){var d;b.client.mainAppWebInfo=null!=(d=b.client.mainAppWebInfo)?
d:{};b.client.mainAppWebInfo.webDisplayMode=em()}(d=E("yt.embedded_player.embed_url"))&&b&&(b.thirdParty={embedUrl:d});var e;if(U("web_log_memory_total_kbytes")&&(null==(e=B.navigator)?0:e.deviceMemory)){var f;e=null==(f=B.navigator)?void 0:f.deviceMemory;b&&(b.client.memoryTotalKbytes=""+1E6*e)}a.appInstallData&&b&&(b.client.configInfo=b.client.configInfo||{},b.client.configInfo.appInstallData=a.appInstallData);(a=zm())&&b&&(b.client.connectionType=a);U("web_log_effective_connection_type")&&(a=Am())&&
b&&(b.client.effectiveConnectionType=a);U("start_client_gcf")&&(e=hp())&&(a=e.coldConfigData,f=e.coldHashData,e=e.hotHashData,b&&(b.client.configInfo=b.client.configInfo||{},a&&(b.client.configInfo.coldConfigData=a),f&&(b.client.configInfo.coldHashData=f),e&&(b.client.configInfo.hotHashData=e)));T("DELEGATED_SESSION_ID")&&!U("pageid_as_header_web")&&(b.user={onBehalfOfUser:T("DELEGATED_SESSION_ID")});!U("fill_delegate_context_in_gel_killswitch")&&(a=T("INNERTUBE_CONTEXT_SERIALIZED_DELEGATION_CONTEXT"))&&
(b.user=Object.assign({},b.user,{serializedDelegationContext:a}));a=Object;f=a.assign;e=b.client;d={};c=x(Object.entries(ol(T("DEVICE",""))));for(var g=c.next();!g.done;g=c.next()){var h=x(g.value);g=h.next().value;h=h.next().value;"cbrand"===g?d.deviceMake=h:"cmodel"===g?d.deviceModel=h:"cbr"===g?d.browserName=h:"cbrver"===g?d.browserVersion=h:"cos"===g?d.osName=h:"cosver"===g?d.osVersion=h:"cplatform"===g&&(d.platform=h)}b.client=f.call(a,e,d);return b}
function lp(a,b,c){c=void 0===c?{}:c;var d={};T("EOM_VISITOR_DATA")?d={"X-Goog-EOM-Visitor-Id":T("EOM_VISITOR_DATA")}:d={"X-Goog-Visitor-Id":c.visitorData||T("VISITOR_DATA","")};if(b&&b.includes("www.youtube-nocookie.com"))return d;b=c.authorization||T("AUTHORIZATION");b||(a?b="Bearer "+E("gapi.auth.getToken")().Cg:(a=hm(gm()),U("pageid_as_header_web")||delete a["X-Goog-PageId"],d=Object.assign({},d,a)));b&&(d.Authorization=b);return d}
;var mp="undefined"!==typeof TextEncoder?new TextEncoder:null,np=mp?function(a){return mp.encode(a)}:function(a){for(var b=[],c=0,d=0;d<a.length;d++){var e=a.charCodeAt(d);
128>e?b[c++]=e:(2048>e?b[c++]=e>>6|192:(55296==(e&64512)&&d+1<a.length&&56320==(a.charCodeAt(d+1)&64512)?(e=65536+((e&1023)<<10)+(a.charCodeAt(++d)&1023),b[c++]=e>>18|240,b[c++]=e>>12&63|128):b[c++]=e>>12|224,b[c++]=e>>6&63|128),b[c++]=e&63|128)}a=new Uint8Array(b.length);for(c=0;c<a.length;c++)a[c]=b[c];return a};function op(a,b){this.version=a;this.args=b}
op.prototype.serialize=function(){return{version:this.version,args:this.args}};function pp(a,b){this.topic=a;this.h=b}
pp.prototype.toString=function(){return this.topic};var qp=E("ytPubsub2Pubsub2Instance")||new M;M.prototype.subscribe=M.prototype.subscribe;M.prototype.unsubscribeByKey=M.prototype.Bb;M.prototype.publish=M.prototype.Ya;M.prototype.clear=M.prototype.clear;D("ytPubsub2Pubsub2Instance",qp);var rp=E("ytPubsub2Pubsub2SubscribedKeys")||{};D("ytPubsub2Pubsub2SubscribedKeys",rp);var sp=E("ytPubsub2Pubsub2TopicToKeys")||{};D("ytPubsub2Pubsub2TopicToKeys",sp);var tp=E("ytPubsub2Pubsub2IsAsync")||{};D("ytPubsub2Pubsub2IsAsync",tp);
D("ytPubsub2Pubsub2SkipSubKey",null);function up(a,b){var c=vp();c&&c.publish.call(c,a.toString(),a,b)}
function wp(a){var b=xp,c=vp();if(!c)return 0;var d=c.subscribe(b.toString(),function(e,f){var g=E("ytPubsub2Pubsub2SkipSubKey");g&&g==d||(g=function(){if(rp[d])try{if(f&&b instanceof pp&&b!=e)try{var h=b.h,k=f;if(!k.args||!k.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");try{if(!h.Ed){var l=new h;h.Ed=l.version}var n=h.Ed}catch(C){}if(!n||k.version!=n)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");try{n=Reflect;var p=n.construct;
var r=k.args,t=r.length;if(0<t){var v=Array(t);for(k=0;k<t;k++)v[k]=r[k];var w=v}else w=[];f=p.call(n,h,w)}catch(C){throw C.message="yt.pubsub2.Data.deserialize(): "+C.message,C;}}catch(C){throw C.message="yt.pubsub2.pubsub2 cross-binary conversion error for "+b.toString()+": "+C.message,C;}a.call(window,f)}catch(C){gl(C)}},tp[b.toString()]?E("yt.scheduler.instance")?Pi.pa(g):xl(g,0):g())});
rp[d]=!0;sp[b.toString()]||(sp[b.toString()]=[]);sp[b.toString()].push(d);return d}
function yp(){var a=zp,b=wp(function(c){a.apply(void 0,arguments);Ap(b)});
return b}
function Ap(a){var b=vp();b&&("number"===typeof a&&(a=[a]),Db(a,function(c){b.unsubscribeByKey(c);delete rp[c]}))}
function vp(){return E("ytPubsub2Pubsub2Instance")}
;function Bp(a,b,c){c=void 0===c?{sampleRate:.1}:c;Math.random()<Math.min(.02,c.sampleRate/100)&&up("meta_logging_csi_event",{timerName:a,ah:b})}
;var Cp=void 0,Dp=void 0;function Ep(){Dp||(Dp=Dk(T("WORKER_SERIALIZATION_URL")));return Dp||void 0}
function Fp(){var a=Ep();Cp||void 0===a||(Cp=new Worker(kb(a),void 0));return Cp}
;var Gp=Al("max_body_size_to_compress",5E5),Hp=Al("min_body_size_to_compress",500),Ip=!0,Jp=0,Kp=0,Lp=Al("compression_performance_threshold_lr",250),Mp=Al("slow_compressions_before_abandon_count",4),Np=!1,Op=new Map,Pp=1,Qp=!0;function Rp(){if("function"===typeof Worker&&Ep()&&!Np){var a=function(c){c=c.data;if("gzippedGelBatch"===c.op){var d=Op.get(c.key);d&&(Sp(c.gzippedBatch,d.latencyPayload,d.url,d.options,d.sendFn),Op.delete(c.key))}},b=Fp();
b&&(b.addEventListener("message",a),b.onerror=function(){Op.clear()},Np=!0)}}
function Tp(a,b,c,d,e){e=void 0===e?!1:e;var f={startTime:W(),ticks:{},infos:{}};if(Ip)try{var g=Up(b);if(null!=g&&(g>Gp||g<Hp))d(a,c);else{if(U("gzip_gel_with_worker")&&(U("initial_gzip_use_main_thread")&&!Qp||!U("initial_gzip_use_main_thread"))){Np||Rp();var h=Fp();if(h&&!e){Op.set(Pp,{latencyPayload:f,url:a,options:c,sendFn:d});h.postMessage({op:"gelBatchToGzip",serializedBatch:b,key:Pp});Pp++;return}}var k=Ck(np(b));Sp(k,f,a,c,d)}}catch(l){hl(l),d(a,c)}else d(a,c)}
function Sp(a,b,c,d,e){Qp=!1;var f=W();b.ticks.gelc=f;Kp++;U("disable_compression_due_to_performance_degredation")&&f-b.startTime>=Lp&&(Jp++,U("abandon_compression_after_N_slow_zips")?Kp===Al("compression_disable_point")&&Jp>Mp&&(Ip=!1):Ip=!1);Vp(b);d.headers||(d.headers={});d.headers["Content-Encoding"]="gzip";d.postBody=a;d.postParams=void 0;e(c,d)}
function Wp(a){var b=void 0===b?!1:b;var c=void 0===c?!1:c;var d=W(),e={startTime:d,ticks:{},infos:{}},f=b?E("yt.logging.gzipForFetch",!1):!0;if(Ip&&f){if(!a.body)return a;try{var g=c?a.body:"string"===typeof a.body?a.body:JSON.stringify(a.body);f=g;if(!c&&"string"===typeof g){var h=Up(g);if(null!=h&&(h>Gp||h<Hp))return a;c=b?{level:1}:void 0;f=Ck(np(g),c);var k=W();e.ticks.gelc=k;if(b){Kp++;if((U("disable_compression_due_to_performance_degredation")||U("disable_compression_due_to_performance_degradation_lr"))&&
k-d>=Lp)if(Jp++,U("abandon_compression_after_N_slow_zips")||U("abandon_compression_after_N_slow_zips_lr")){b=Jp/Kp;var l=Mp/Al("compression_disable_point");0<Kp&&0===Kp%Al("compression_disable_point")&&b>=l&&(Ip=!1)}else Ip=!1;Vp(e)}}a.headers=Object.assign({},{"Content-Encoding":"gzip"},a.headers||{});a.body=f;return a}catch(n){return hl(n),a}}else return a}
function Up(a){try{return(new Blob(a.split(""))).size}catch(b){return hl(b),null}}
function Vp(a){U("gel_compression_csi_killswitch")||!U("log_gel_compression_latency")&&!U("log_gel_compression_latency_lr")||Bp("gel_compression",a,{sampleRate:.1})}
;function Xp(a){a=Object.assign({},a);delete a.Authorization;var b=oh();if(b){var c=new Ti;c.update(T("INNERTUBE_API_KEY"));c.update(b);a.hash=Ie(c.digest(),3)}return a}
;var Yp;function Zp(){Yp||(Yp=new kn("yt.innertube"));return Yp}
function $p(a,b,c,d){if(d)return null;d=Zp().get("nextId",!0)||1;var e=Zp().get("requests",!0)||{};e[d]={method:a,request:b,authState:Xp(c),requestTime:Math.round(W())};Zp().set("nextId",d+1,86400,!0);Zp().set("requests",e,86400,!0);return d}
function aq(a){var b=Zp().get("requests",!0)||{};delete b[a];Zp().set("requests",b,86400,!0)}
function bq(a){var b=Zp().get("requests",!0);if(b){for(var c in b){var d=b[c];if(!(6E4>Math.round(W())-d.requestTime)){var e=d.authState,f=Xp(lp(!1));Qb(e,f)&&(e=d.request,"requestTimeMs"in e&&(e.requestTimeMs=Math.round(W())),cq(a,d.method,e,{}));delete b[c]}}Zp().set("requests",b,86400,!0)}}
;function dq(a){this.Yb=this.h=!1;this.potentialEsfErrorCounter=this.i=0;this.handleError=function(){};
this.pb=function(){};
this.now=Date.now;this.Ib=!1;var b;this.Bd=null!=(b=a.Bd)?b:100;var c;this.vd=null!=(c=a.vd)?c:1;var d;this.sd=null!=(d=a.sd)?d:2592E6;var e;this.qd=null!=(e=a.qd)?e:12E4;var f;this.ud=null!=(f=a.ud)?f:5E3;var g;this.X=null!=(g=a.X)?g:void 0;this.ec=!!a.ec;var h;this.cc=null!=(h=a.cc)?h:.1;var k;this.mc=null!=(k=a.mc)?k:10;a.handleError&&(this.handleError=a.handleError);a.pb&&(this.pb=a.pb);a.Ib&&(this.Ib=a.Ib);a.Yb&&(this.Yb=a.Yb);this.Y=a.Y;this.Da=a.Da;this.ha=a.ha;this.fa=a.fa;this.sendFn=a.sendFn;
this.Kc=a.Kc;this.Hc=a.Hc;eq(this)&&(!this.Y||this.Y("networkless_logging"))&&fq(this)}
function fq(a){eq(a)&&!a.Ib&&(a.h=!0,a.ec&&Math.random()<=a.cc&&a.ha.Qd(a.X),gq(a),a.fa.va()&&a.Tb(),a.fa.listen(a.Kc,a.Tb.bind(a)),a.fa.listen(a.Hc,a.Vc.bind(a)))}
m=dq.prototype;m.writeThenSend=function(a,b){var c=this;b=void 0===b?{}:b;if(eq(this)&&this.h){var d={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0};this.ha.set(d,this.X).then(function(e){d.id=e;c.fa.va()&&hq(c,d)}).catch(function(e){hq(c,d);
iq(c,e)})}else this.sendFn(a,b)};
m.sendThenWrite=function(a,b,c){var d=this;b=void 0===b?{}:b;if(eq(this)&&this.h){var e={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0};this.Y&&this.Y("nwl_skip_retry")&&(e.skipRetry=c);if(this.fa.va()||this.Y&&this.Y("nwl_aggressive_send_then_write")&&!e.skipRetry){if(!e.skipRetry){var f=b.onError?b.onError:function(){};
b.onError=function(g,h){return z(function(k){if(1==k.h)return k.yield(d.ha.set(e,d.X).catch(function(l){iq(d,l)}),2);
f(g,h);k.h=0})}}this.sendFn(a,b,e.skipRetry)}else this.ha.set(e,this.X).catch(function(g){d.sendFn(a,b,e.skipRetry);
iq(d,g)})}else this.sendFn(a,b,this.Y&&this.Y("nwl_skip_retry")&&c)};
m.sendAndWrite=function(a,b){var c=this;b=void 0===b?{}:b;if(eq(this)&&this.h){var d={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0},e=!1,f=b.onSuccess?b.onSuccess:function(){};
d.options.onSuccess=function(g,h){void 0!==d.id?c.ha.ob(d.id,c.X):e=!0;c.fa.gb&&c.Y&&c.Y("vss_network_hint")&&c.fa.gb(!0);f(g,h)};
this.sendFn(d.url,d.options,void 0,!0);this.ha.set(d,this.X).then(function(g){d.id=g;e&&c.ha.ob(d.id,c.X)}).catch(function(g){iq(c,g)})}else this.sendFn(a,b,void 0,!0)};
m.Tb=function(){var a=this;if(!eq(this))throw Error("IndexedDB is not supported: throttleSend");this.i||(this.i=this.Da.pa(function(){var b;return z(function(c){if(1==c.h)return c.yield(a.ha.dd("NEW",a.X),2);if(3!=c.h)return b=c.i,b?c.yield(hq(a,b),3):(a.Vc(),c.return());a.i&&(a.i=0,a.Tb());c.h=0})},this.Bd))};
m.Vc=function(){this.Da.qa(this.i);this.i=0};
function hq(a,b){var c;return z(function(d){switch(d.h){case 1:if(!eq(a))throw Error("IndexedDB is not supported: immediateSend");if(void 0===b.id){d.B(2);break}return d.yield(a.ha.te(b.id,a.X),3);case 3:(c=d.i)||a.pb(Error("The request cannot be found in the database."));case 2:if(jq(a,b,a.sd)){d.B(4);break}a.pb(Error("Networkless Logging: Stored logs request expired age limit"));if(void 0===b.id){d.B(5);break}return d.yield(a.ha.ob(b.id,a.X),5);case 5:return d.return();case 4:b.skipRetry||(b=kq(a,
b));if(!b){d.B(0);break}if(!b.skipRetry||void 0===b.id){d.B(8);break}return d.yield(a.ha.ob(b.id,a.X),8);case 8:a.sendFn(b.url,b.options,!!b.skipRetry),d.h=0}})}
function kq(a,b){if(!eq(a))throw Error("IndexedDB is not supported: updateRequestHandlers");var c=b.options.onError?b.options.onError:function(){};
b.options.onError=function(e,f){var g,h,k,l;return z(function(n){switch(n.h){case 1:g=lq(f);(h=mq(f))&&a.Y&&a.Y("web_enable_error_204")&&a.handleError(Error("Request failed due to compression"),b.url,f);if(!(a.Y&&a.Y("nwl_consider_error_code")&&g||a.Y&&!a.Y("nwl_consider_error_code")&&a.potentialEsfErrorCounter<=a.mc)){n.B(2);break}if(!a.fa.pc){n.B(3);break}return n.yield(a.fa.pc(),3);case 3:if(a.fa.va()){n.B(2);break}c(e,f);if(!a.Y||!a.Y("nwl_consider_error_code")||void 0===(null==(k=b)?void 0:k.id)){n.B(6);
break}return n.yield(a.ha.Lc(b.id,a.X,!1),6);case 6:return n.return();case 2:if(a.Y&&a.Y("nwl_consider_error_code")&&!g&&a.potentialEsfErrorCounter>a.mc)return n.return();a.potentialEsfErrorCounter++;if(void 0===(null==(l=b)?void 0:l.id)){n.B(8);break}return b.sendCount<a.vd?n.yield(a.ha.Lc(b.id,a.X,!0,h?!1:void 0),12):n.yield(a.ha.ob(b.id,a.X),8);case 12:a.Da.pa(function(){a.fa.va()&&a.Tb()},a.ud);
case 8:c(e,f),n.h=0}})};
var d=b.options.onSuccess?b.options.onSuccess:function(){};
b.options.onSuccess=function(e,f){var g;return z(function(h){if(1==h.h)return void 0===(null==(g=b)?void 0:g.id)?h.B(2):h.yield(a.ha.ob(b.id,a.X),2);a.fa.gb&&a.Y&&a.Y("vss_network_hint")&&a.fa.gb(!0);d(e,f);h.h=0})};
return b}
function jq(a,b,c){b=b.timestamp;return a.now()-b>=c?!1:!0}
function gq(a){if(!eq(a))throw Error("IndexedDB is not supported: retryQueuedRequests");a.ha.dd("QUEUED",a.X).then(function(b){b&&!jq(a,b,a.qd)?a.Da.pa(function(){return z(function(c){if(1==c.h)return void 0===b.id?c.B(2):c.yield(a.ha.Lc(b.id,a.X),2);gq(a);c.h=0})}):a.fa.va()&&a.Tb()})}
function iq(a,b){a.Hd&&!a.fa.va()?a.Hd(b):a.handleError(b)}
function eq(a){return!!a.X||a.Yb}
function lq(a){var b;return(a=null==a?void 0:null==(b=a.error)?void 0:b.code)&&400<=a&&599>=a?!1:!0}
function mq(a){var b;a=null==a?void 0:null==(b=a.error)?void 0:b.code;return!(400!==a&&415!==a)}
;var nq;
function oq(){if(nq)return nq();var a={};nq=Vo("LogsDatabaseV2",{xb:(a.LogsRequestsStore={Fb:2},a),shared:!1,upgrade:function(b,c,d){c(2)&&$n(b,"LogsRequestsStore",{keyPath:"id",autoIncrement:!0});c(3);c(5)&&(d=d.objectStore("LogsRequestsStore"),d.h.indexNames.contains("newRequest")&&d.h.deleteIndex("newRequest"),ho(d,"newRequestV2",["status","interface","timestamp"]));c(7)&&b.h.objectStoreNames.contains("sapisid")&&b.h.deleteObjectStore("sapisid");c(9)&&b.h.objectStoreNames.contains("SWHealthLog")&&b.h.deleteObjectStore("SWHealthLog")},
version:9});return nq()}
;function pq(a){return uo(oq(),a)}
function qq(a,b){var c,d,e,f;return z(function(g){if(1==g.h)return c={startTime:W(),infos:{transactionType:"YT_IDB_TRANSACTION_TYPE_WRITE"},ticks:{}},g.yield(pq(b),2);if(3!=g.h)return d=g.i,e=Object.assign({},a,{options:JSON.parse(JSON.stringify(a.options)),interface:T("INNERTUBE_CONTEXT_CLIENT_NAME",0)}),g.yield(bo(d,"LogsRequestsStore",e),3);f=g.i;c.ticks.tc=W();rq(c);return g.return(f)})}
function sq(a,b){var c,d,e,f,g,h,k,l;return z(function(n){if(1==n.h)return c={startTime:W(),infos:{transactionType:"YT_IDB_TRANSACTION_TYPE_READ"},ticks:{}},n.yield(pq(b),2);if(3!=n.h)return d=n.i,e=T("INNERTUBE_CONTEXT_CLIENT_NAME",0),f=[a,e,0],g=[a,e,W()],h=IDBKeyRange.bound(f,g),k="prev",U("use_fifo_for_networkless")&&(k="next"),l=void 0,n.yield(Zn(d,["LogsRequestsStore"],{mode:"readwrite",la:!0},function(p){return no(p.objectStore("LogsRequestsStore").index("newRequestV2"),{query:h,direction:k},
function(r){r.getValue()&&(l=r.getValue(),"NEW"===a&&(l.status="QUEUED",r.update(l)))})}),3);
c.ticks.tc=W();rq(c);return n.return(l)})}
function tq(a,b){var c;return z(function(d){if(1==d.h)return d.yield(pq(b),2);c=d.i;return d.return(Zn(c,["LogsRequestsStore"],{mode:"readwrite",la:!0},function(e){var f=e.objectStore("LogsRequestsStore");return f.get(a).then(function(g){if(g)return g.status="QUEUED",Vn(f.h.put(g,void 0)).then(function(){return g})})}))})}
function uq(a,b,c,d){c=void 0===c?!0:c;var e;return z(function(f){if(1==f.h)return f.yield(pq(b),2);e=f.i;return f.return(Zn(e,["LogsRequestsStore"],{mode:"readwrite",la:!0},function(g){var h=g.objectStore("LogsRequestsStore");return h.get(a).then(function(k){return k?(k.status="NEW",c&&(k.sendCount+=1),void 0!==d&&(k.options.compress=d),Vn(h.h.put(k,void 0)).then(function(){return k})):Pn.resolve(void 0)})}))})}
function vq(a,b){var c;return z(function(d){if(1==d.h)return d.yield(pq(b),2);c=d.i;return d.return(c.delete("LogsRequestsStore",a))})}
function wq(a){var b,c;return z(function(d){if(1==d.h)return d.yield(pq(a),2);b=d.i;c=W()-2592E6;return d.yield(Zn(b,["LogsRequestsStore"],{mode:"readwrite",la:!0},function(e){return jo(e.objectStore("LogsRequestsStore"),{},function(f){if(f.getValue().timestamp<=c)return f.delete().then(function(){return ko(f)})})}),0)})}
function xq(){z(function(a){return a.yield(Ro(),0)})}
function rq(a){U("nwl_csi_killswitch")||Bp("networkless_performance",a,{sampleRate:1})}
;var yq={accountStateChangeSignedIn:23,accountStateChangeSignedOut:24,delayedEventMetricCaptured:11,latencyActionBaselined:6,latencyActionInfo:7,latencyActionTicked:5,offlineTransferStatusChanged:2,offlineImageDownload:335,playbackStartStateChanged:9,systemHealthCaptured:3,mangoOnboardingCompleted:10,mangoPushNotificationReceived:230,mangoUnforkDbMigrationError:121,mangoUnforkDbMigrationSummary:122,mangoUnforkDbMigrationPreunforkDbVersionNumber:133,mangoUnforkDbMigrationPhoneMetadata:134,mangoUnforkDbMigrationPhoneStorage:135,
mangoUnforkDbMigrationStep:142,mangoAsyncApiMigrationEvent:223,mangoDownloadVideoResult:224,mangoHomepageVideoCount:279,mangoHomeV3State:295,mangoImageClientCacheHitEvent:273,sdCardStatusChanged:98,framesDropped:12,thumbnailHovered:13,deviceRetentionInfoCaptured:14,thumbnailLoaded:15,backToAppEvent:318,streamingStatsCaptured:17,offlineVideoShared:19,appCrashed:20,youThere:21,offlineStateSnapshot:22,mdxSessionStarted:25,mdxSessionConnected:26,mdxSessionDisconnected:27,bedrockResourceConsumptionSnapshot:28,
nextGenWatchWatchSwiped:29,kidsAccountsSnapshot:30,zeroStepChannelCreated:31,tvhtml5SearchCompleted:32,offlineSharePairing:34,offlineShareUnlock:35,mdxRouteDistributionSnapshot:36,bedrockRepetitiveActionTimed:37,unpluggedDegradationInfo:229,uploadMp4HeaderMoved:38,uploadVideoTranscoded:39,uploadProcessorStarted:46,uploadProcessorEnded:47,uploadProcessorReady:94,uploadProcessorRequirementPending:95,uploadProcessorInterrupted:96,uploadFrontendEvent:241,assetPackDownloadStarted:41,assetPackDownloaded:42,
assetPackApplied:43,assetPackDeleted:44,appInstallAttributionEvent:459,playbackSessionStopped:45,adBlockerMessagingShown:48,distributionChannelCaptured:49,dataPlanCpidRequested:51,detailedNetworkTypeCaptured:52,sendStateUpdated:53,receiveStateUpdated:54,sendDebugStateUpdated:55,receiveDebugStateUpdated:56,kidsErrored:57,mdxMsnSessionStatsFinished:58,appSettingsCaptured:59,mdxWebSocketServerHttpError:60,mdxWebSocketServer:61,startupCrashesDetected:62,coldStartInfo:435,offlinePlaybackStarted:63,liveChatMessageSent:225,
liveChatUserPresent:434,liveChatBeingModerated:457,liveCreationCameraUpdated:64,liveCreationEncodingCaptured:65,liveCreationError:66,liveCreationHealthUpdated:67,liveCreationVideoEffectsCaptured:68,liveCreationStageOccured:75,liveCreationBroadcastScheduled:123,liveCreationArchiveReplacement:149,liveCreationCostreamingConnection:421,liveCreationStreamWebrtcStats:288,mdxSessionRecoveryStarted:69,mdxSessionRecoveryCompleted:70,mdxSessionRecoveryStopped:71,visualElementShown:72,visualElementHidden:73,
visualElementGestured:78,visualElementStateChanged:208,screenCreated:156,playbackAssociated:202,visualElementAttached:215,playbackContextEvent:214,cloudCastingPlaybackStarted:74,webPlayerApiCalled:76,tvhtml5AccountDialogOpened:79,foregroundHeartbeat:80,foregroundHeartbeatScreenAssociated:111,kidsOfflineSnapshot:81,mdxEncryptionSessionStatsFinished:82,playerRequestCompleted:83,liteSchedulerStatistics:84,mdxSignIn:85,spacecastMetadataLookupRequested:86,spacecastBatchLookupRequested:87,spacecastSummaryRequested:88,
spacecastPlayback:89,spacecastDiscovery:90,tvhtml5LaunchUrlComponentChanged:91,mdxBackgroundPlaybackRequestCompleted:92,mdxBrokenAdditionalDataDeviceDetected:93,tvhtml5LocalStorage:97,tvhtml5DeviceStorageStatus:147,autoCaptionsAvailable:99,playbackScrubbingEvent:339,flexyState:100,interfaceOrientationCaptured:101,mainAppBrowseFragmentCache:102,offlineCacheVerificationFailure:103,offlinePlaybackExceptionDigest:217,vrCopresenceStats:104,vrCopresenceSyncStats:130,vrCopresenceCommsStats:137,vrCopresencePartyStats:153,
vrCopresenceEmojiStats:213,vrCopresenceEvent:141,vrCopresenceFlowTransitEvent:160,vrCowatchPartyEvent:492,vrPlaybackEvent:345,kidsAgeGateTracking:105,offlineDelayAllowedTracking:106,mainAppAutoOfflineState:107,videoAsThumbnailDownload:108,videoAsThumbnailPlayback:109,liteShowMore:110,renderingError:118,kidsProfilePinGateTracking:119,abrTrajectory:124,scrollEvent:125,streamzIncremented:126,kidsProfileSwitcherTracking:127,kidsProfileCreationTracking:129,buyFlowStarted:136,mbsConnectionInitiated:138,
mbsPlaybackInitiated:139,mbsLoadChildren:140,liteProfileFetcher:144,mdxRemoteTransaction:146,reelPlaybackError:148,reachabilityDetectionEvent:150,mobilePlaybackEvent:151,courtsidePlayerStateChanged:152,musicPersistentCacheChecked:154,musicPersistentCacheCleared:155,playbackInterrupted:157,playbackInterruptionResolved:158,fixFopFlow:159,anrDetection:161,backstagePostCreationFlowEnded:162,clientError:163,gamingAccountLinkStatusChanged:164,liteHousewarming:165,buyFlowEvent:167,kidsParentalGateTracking:168,
kidsSignedOutSettingsStatus:437,kidsSignedOutPauseHistoryFixStatus:438,tvhtml5WatchdogViolation:444,ypcUpgradeFlow:169,yongleStudy:170,ypcUpdateFlowStarted:171,ypcUpdateFlowCancelled:172,ypcUpdateFlowSucceeded:173,ypcUpdateFlowFailed:174,liteGrowthkitPromo:175,paymentFlowStarted:341,transactionFlowShowPaymentDialog:405,transactionFlowStarted:176,transactionFlowSecondaryDeviceStarted:222,transactionFlowSecondaryDeviceSignedOutStarted:383,transactionFlowCancelled:177,transactionFlowPaymentCallBackReceived:387,
transactionFlowPaymentSubmitted:460,transactionFlowPaymentSucceeded:329,transactionFlowSucceeded:178,transactionFlowFailed:179,transactionFlowPlayBillingConnectionStartEvent:428,transactionFlowSecondaryDeviceSuccess:458,transactionFlowErrorEvent:411,liteVideoQualityChanged:180,watchBreakEnablementSettingEvent:181,watchBreakFrequencySettingEvent:182,videoEffectsCameraPerformanceMetrics:183,adNotify:184,startupTelemetry:185,playbackOfflineFallbackUsed:186,outOfMemory:187,ypcPauseFlowStarted:188,ypcPauseFlowCancelled:189,
ypcPauseFlowSucceeded:190,ypcPauseFlowFailed:191,uploadFileSelected:192,ypcResumeFlowStarted:193,ypcResumeFlowCancelled:194,ypcResumeFlowSucceeded:195,ypcResumeFlowFailed:196,adsClientStateChange:197,ypcCancelFlowStarted:198,ypcCancelFlowCancelled:199,ypcCancelFlowSucceeded:200,ypcCancelFlowFailed:201,ypcCancelFlowGoToPaymentProcessor:402,ypcDeactivateFlowStarted:320,ypcRedeemFlowStarted:203,ypcRedeemFlowCancelled:204,ypcRedeemFlowSucceeded:205,ypcRedeemFlowFailed:206,ypcFamilyCreateFlowStarted:258,
ypcFamilyCreateFlowCancelled:259,ypcFamilyCreateFlowSucceeded:260,ypcFamilyCreateFlowFailed:261,ypcFamilyManageFlowStarted:262,ypcFamilyManageFlowCancelled:263,ypcFamilyManageFlowSucceeded:264,ypcFamilyManageFlowFailed:265,restoreContextEvent:207,embedsAdEvent:327,autoplayTriggered:209,clientDataErrorEvent:210,experimentalVssValidation:211,tvhtml5TriggeredEvent:212,tvhtml5FrameworksFieldTrialResult:216,tvhtml5FrameworksFieldTrialStart:220,musicOfflinePreferences:218,watchTimeSegment:219,appWidthLayoutError:221,
accountRegistryChange:226,userMentionAutoCompleteBoxEvent:227,downloadRecommendationEnablementSettingEvent:228,musicPlaybackContentModeChangeEvent:231,offlineDbOpenCompleted:232,kidsFlowEvent:233,kidsFlowCorpusSelectedEvent:234,videoEffectsEvent:235,unpluggedOpsEogAnalyticsEvent:236,playbackAudioRouteEvent:237,interactionLoggingDebugModeError:238,offlineYtbRefreshed:239,kidsFlowError:240,musicAutoplayOnLaunchAttempted:242,deviceContextActivityEvent:243,deviceContextEvent:244,templateResolutionException:245,
musicSideloadedPlaylistServiceCalled:246,embedsStorageAccessNotChecked:247,embedsHasStorageAccessResult:248,embedsItpPlayedOnReload:249,embedsRequestStorageAccessResult:250,embedsShouldRequestStorageAccessResult:251,embedsRequestStorageAccessState:256,embedsRequestStorageAccessFailedState:257,embedsItpWatchLaterResult:266,searchSuggestDecodingPayloadFailure:252,siriShortcutActivated:253,tvhtml5KeyboardPerformance:254,latencyActionSpan:255,elementsLog:267,ytbFileOpened:268,tfliteModelError:269,apiTest:270,
yongleUsbSetup:271,touStrikeInterstitialEvent:272,liteStreamToSave:274,appBundleClientEvent:275,ytbFileCreationFailed:276,adNotifyFailure:278,ytbTransferFailed:280,blockingRequestFailed:281,liteAccountSelector:282,liteAccountUiCallbacks:283,dummyPayload:284,browseResponseValidationEvent:285,entitiesError:286,musicIosBackgroundFetch:287,mdxNotificationEvent:289,layersValidationError:290,musicPwaInstalled:291,liteAccountCleanup:292,html5PlayerHealthEvent:293,watchRestoreAttempt:294,liteAccountSignIn:296,
notaireEvent:298,kidsVoiceSearchEvent:299,adNotifyFilled:300,delayedEventDropped:301,analyticsSearchEvent:302,systemDarkThemeOptOutEvent:303,flowEvent:304,networkConnectivityBaselineEvent:305,ytbFileImported:306,downloadStreamUrlExpired:307,directSignInEvent:308,lyricImpressionEvent:309,accessibilityStateEvent:310,tokenRefreshEvent:311,genericAttestationExecution:312,tvhtml5VideoSeek:313,unpluggedAutoPause:314,scrubbingEvent:315,bedtimeReminderEvent:317,tvhtml5UnexpectedRestart:319,tvhtml5StabilityTraceEvent:478,
tvhtml5OperationHealth:467,tvhtml5WatchKeyEvent:321,voiceLanguageChanged:322,tvhtml5LiveChatStatus:323,parentToolsCorpusSelectedEvent:324,offerAdsEnrollmentInitiated:325,networkQualityIntervalEvent:326,deviceStartupMetrics:328,heartbeatActionPlayerTransitioned:330,tvhtml5Lifecycle:331,heartbeatActionPlayerHalted:332,adaptiveInlineMutedSettingEvent:333,mainAppLibraryLoadingState:334,thirdPartyLogMonitoringEvent:336,appShellAssetLoadReport:337,tvhtml5AndroidAttestation:338,tvhtml5StartupSoundEvent:340,
iosBackgroundRefreshTask:342,iosBackgroundProcessingTask:343,sliEventBatch:344,postImpressionEvent:346,musicSideloadedPlaylistExport:347,idbUnexpectedlyClosed:348,voiceSearchEvent:349,mdxSessionCastEvent:350,idbQuotaExceeded:351,idbTransactionEnded:352,idbTransactionAborted:353,tvhtml5KeyboardLogging:354,idbIsSupportedCompleted:355,creatorStudioMobileEvent:356,idbDataCorrupted:357,parentToolsAppChosenEvent:358,webViewBottomSheetResized:359,activeStateControllerScrollPerformanceSummary:360,navigatorValidation:361,
mdxSessionHeartbeat:362,clientHintsPolyfillDiagnostics:363,clientHintsPolyfillEvent:364,proofOfOriginTokenError:365,kidsAddedAccountSummary:366,musicWearableDevice:367,ypcRefundFlowEvent:368,tvhtml5PlaybackMeasurementEvent:369,tvhtml5WatermarkMeasurementEvent:370,clientExpGcfPropagationEvent:371,mainAppReferrerIntent:372,leaderLockEnded:373,leaderLockAcquired:374,googleHatsEvent:375,persistentLensLaunchEvent:376,parentToolsChildWelcomeChosenEvent:378,browseThumbnailPreloadEvent:379,finalPayload:380,
mdxDialAdditionalDataUpdateEvent:381,webOrchestrationTaskLifecycleRecord:382,startupSignalEvent:384,accountError:385,gmsDeviceCheckEvent:386,accountSelectorEvent:388,accountUiCallbacks:389,mdxDialAdditionalDataProbeEvent:390,downloadsSearchIcingApiStats:391,downloadsSearchIndexUpdatedEvent:397,downloadsSearchIndexSnapshot:398,dataPushClientEvent:392,kidsCategorySelectedEvent:393,mdxDeviceManagementSnapshotEvent:394,prefetchRequested:395,prefetchableCommandExecuted:396,gelDebuggingEvent:399,webLinkTtsPlayEnd:400,
clipViewInvalid:401,persistentStorageStateChecked:403,cacheWipeoutEvent:404,playerEvent:410,sfvEffectPipelineStartedEvent:412,sfvEffectPipelinePausedEvent:429,sfvEffectPipelineEndedEvent:413,sfvEffectChosenEvent:414,sfvEffectLoadedEvent:415,sfvEffectUserInteractionEvent:465,sfvEffectFirstFrameProcessedLatencyEvent:416,sfvEffectAggregatedFramesProcessedLatencyEvent:417,sfvEffectAggregatedFramesDroppedEvent:418,sfvEffectPipelineErrorEvent:430,sfvEffectGraphFrozenEvent:419,sfvEffectGlThreadBlockedEvent:420,
mdeVideoChangedEvent:442,mdePlayerPerformanceMetrics:472,mdeExporterEvent:497,genericClientExperimentEvent:423,homePreloadTaskScheduled:424,homePreloadTaskExecuted:425,homePreloadCacheHit:426,polymerPropertyChangedInObserver:427,applicationStarted:431,networkCronetRttBatch:432,networkCronetRttSummary:433,repeatChapterLoopEvent:436,seekCancellationEvent:462,lockModeTimeoutEvent:483,externalVideoShareToYoutubeAttempt:501,offlineTransferStarted:4,musicOfflineMixtapePreferencesChanged:16,mangoDailyNewVideosNotificationAttempt:40,
mangoDailyNewVideosNotificationError:77,dtwsPlaybackStarted:112,dtwsTileFetchStarted:113,dtwsTileFetchCompleted:114,dtwsTileFetchStatusChanged:145,dtwsKeyframeDecoderBufferSent:115,dtwsTileUnderflowedOnNonkeyframe:116,dtwsBackfillFetchStatusChanged:143,dtwsBackfillUnderflowed:117,dtwsAdaptiveLevelChanged:128,blockingVisitorIdTimeout:277,liteSocial:18,mobileJsInvocation:297,biscottiBasedDetection:439,coWatchStateChange:440,embedsVideoDataDidChange:441,shortsFirst:443,cruiseControlEvent:445,qoeClientLoggingContext:446,
atvRecommendationJobExecuted:447,tvhtml5UserFeedback:448,producerProjectCreated:449,producerProjectOpened:450,producerProjectDeleted:451,producerProjectElementAdded:453,producerProjectElementRemoved:454,tvhtml5ShowClockEvent:455,deviceCapabilityCheckMetrics:456,youtubeClearcutEvent:461,offlineBrowseFallbackEvent:463,getCtvTokenEvent:464,startupDroppedFramesSummary:466,screenshotEvent:468,miniAppPlayEvent:469,elementsDebugCounters:470,fontLoadEvent:471,webKillswitchReceived:473,webKillswitchExecuted:474,
cameraOpenEvent:475,manualSmoothnessMeasurement:476,tvhtml5AppQualityEvent:477,polymerPropertyAccessEvent:479,miniAppSdkUsage:480,cobaltTelemetryEvent:481,crossDevicePlayback:482,channelCreatedWithObakeImage:484,channelEditedWithObakeImage:485,offlineDeleteEvent:486,crossDeviceNotificationTransfer:487,androidIntentEvent:488,unpluggedAmbientInterludesCounterfactualEvent:489,keyPlaysPlayback:490,shortsCreationFallbackEvent:493,vssData:491,castMatch:494,miniAppPerformanceMetrics:495,userFeedbackEvent:496,
kidsGuestSessionMismatch:498,musicSideloadedPlaylistMigrationEvent:499,sleepTimerSessionFinishEvent:500};var zq={},Aq=Vo("ServiceWorkerLogsDatabase",{xb:(zq.SWHealthLog={Fb:1},zq),shared:!0,upgrade:function(a,b){b(1)&&ho($n(a,"SWHealthLog",{keyPath:"id",autoIncrement:!0}),"swHealthNewRequest",["interface","timestamp"])},
version:1});function Bq(a){return uo(Aq(),a)}
function Cq(a){var b,c;z(function(d){if(1==d.h)return d.yield(Bq(a),2);b=d.i;c=W()-2592E6;return d.yield(Zn(b,["SWHealthLog"],{mode:"readwrite",la:!0},function(e){return jo(e.objectStore("SWHealthLog"),{},function(f){if(f.getValue().timestamp<=c)return f.delete().then(function(){return ko(f)})})}),0)})}
function Dq(a){var b;return z(function(c){if(1==c.h)return c.yield(Bq(a),2);b=c.i;return c.yield(b.clear("SWHealthLog"),0)})}
;var Eq={},Fq=0;function Gq(a){var b=new Image,c=""+Fq++;Eq[c]=b;b.onload=b.onerror=function(){delete Eq[c]};
b.src=a}
;var Hq;function Iq(){Hq||(Hq=new kn("yt.offline"));return Hq}
function Jq(a){if(U("offline_error_handling")){var b=Iq().get("errors",!0)||{};b[a.message]={name:a.name,stack:a.stack};a.level&&(b[a.message].level=a.level);Iq().set("errors",b,2592E3,!0)}}
;function Kq(){this.h=new Map;this.i=!1}
function Lq(){if(!Kq.h){var a=E("yt.networkRequestMonitor.instance")||new Kq;D("yt.networkRequestMonitor.instance",a);Kq.h=a}return Kq.h}
Kq.prototype.requestComplete=function(a,b){b&&(this.i=!0);a=this.removeParams(a);this.h.get(a)||this.h.set(a,b)};
Kq.prototype.isEndpointCFR=function(a){a=this.removeParams(a);return(a=this.h.get(a))?!1:!1===a&&this.i?!0:null};
Kq.prototype.removeParams=function(a){return a.split("?")[0]};
Kq.prototype.removeParams=Kq.prototype.removeParams;Kq.prototype.isEndpointCFR=Kq.prototype.isEndpointCFR;Kq.prototype.requestComplete=Kq.prototype.requestComplete;Kq.getInstance=Lq;function Mq(){wd.call(this);var a=this;this.j=!1;this.i=Oi();this.i.listen("networkstatus-online",function(){if(a.j&&U("offline_error_handling")){var b=Iq().get("errors",!0);if(b){for(var c in b)if(b[c]){var d=new V(c,"sent via offline_errors");d.name=b[c].name;d.stack=b[c].stack;d.level=b[c].level;gl(d)}Iq().set("errors",{},2592E3,!0)}}})}
y(Mq,wd);function Nq(){if(!Mq.h){var a=E("yt.networkStatusManager.instance")||new Mq;D("yt.networkStatusManager.instance",a);Mq.h=a}return Mq.h}
m=Mq.prototype;m.va=function(){return this.i.va()};
m.gb=function(a){this.i.i=a};
m.ee=function(){var a=window.navigator.onLine;return void 0===a?!0:a};
m.Vd=function(){this.j=!0};
m.listen=function(a,b){return this.i.listen(a,b)};
m.pc=function(a){a=Mi(this.i,a);a.then(function(b){U("use_cfr_monitor")&&Lq().requestComplete("generate_204",b)});
return a};
Mq.prototype.sendNetworkCheckRequest=Mq.prototype.pc;Mq.prototype.listen=Mq.prototype.listen;Mq.prototype.enableErrorFlushing=Mq.prototype.Vd;Mq.prototype.getWindowStatus=Mq.prototype.ee;Mq.prototype.networkStatusHint=Mq.prototype.gb;Mq.prototype.isNetworkAvailable=Mq.prototype.va;Mq.getInstance=Nq;function Oq(a){a=void 0===a?{}:a;wd.call(this);var b=this;this.i=this.m=0;this.j=Nq();var c=E("yt.networkStatusManager.instance.listen").bind(this.j);c&&(a.rateLimit?(this.rateLimit=a.rateLimit,c("networkstatus-online",function(){Pq(b,"publicytnetworkstatus-online")}),c("networkstatus-offline",function(){Pq(b,"publicytnetworkstatus-offline")})):(c("networkstatus-online",function(){xd(b,"publicytnetworkstatus-online")}),c("networkstatus-offline",function(){xd(b,"publicytnetworkstatus-offline")})))}
y(Oq,wd);Oq.prototype.va=function(){var a=E("yt.networkStatusManager.instance.isNetworkAvailable");return a?a.bind(this.j)():!0};
Oq.prototype.gb=function(a){var b=E("yt.networkStatusManager.instance.networkStatusHint").bind(this.j);b&&b(a)};
Oq.prototype.pc=function(a){var b=this,c;return z(function(d){c=E("yt.networkStatusManager.instance.sendNetworkCheckRequest").bind(b.j);return U("skip_network_check_if_cfr")&&Lq().isEndpointCFR("generate_204")?d.return(new Promise(function(e){var f;b.gb((null==(f=window.navigator)?void 0:f.onLine)||!0);e(b.va())})):c?d.return(c(a)):d.return(!0)})};
function Pq(a,b){a.rateLimit?a.i?(Pi.qa(a.m),a.m=Pi.pa(function(){a.l!==b&&(xd(a,b),a.l=b,a.i=W())},a.rateLimit-(W()-a.i))):(xd(a,b),a.l=b,a.i=W()):xd(a,b)}
;var Qq;function Rq(){var a=dq.call;Qq||(Qq=new Oq({Pg:!0,Ig:!0}));a.call(dq,this,{ha:{Qd:wq,ob:vq,dd:sq,te:tq,Lc:uq,set:qq},fa:Qq,handleError:function(b,c,d){var e,f=null==d?void 0:null==(e=d.error)?void 0:e.code;if(400===f||415===f){var g;hl(new V(b.message,c,null==d?void 0:null==(g=d.error)?void 0:g.code),void 0,void 0,void 0,!0)}else gl(b)},
pb:hl,sendFn:Sq,now:W,Hd:Jq,Da:jn(),Kc:"publicytnetworkstatus-online",Hc:"publicytnetworkstatus-offline",ec:!0,cc:.1,mc:Al("potential_esf_error_limit",10),Y:U,Ib:!(Bm()&&Tq())});this.j=new yi;U("networkless_immediately_drop_all_requests")&&xq();So("LogsDatabaseV2")}
y(Rq,dq);function Uq(){var a=E("yt.networklessRequestController.instance");a||(a=new Rq,D("yt.networklessRequestController.instance",a),U("networkless_logging")&&Ho().then(function(b){a.X=b;fq(a);a.j.resolve();a.ec&&Math.random()<=a.cc&&a.X&&Cq(a.X);U("networkless_immediately_drop_sw_health_store")&&Vq(a)}));
return a}
Rq.prototype.writeThenSend=function(a,b){b||(b={});b=Wq(a,b);Bm()||(this.h=!1);dq.prototype.writeThenSend.call(this,a,b)};
Rq.prototype.sendThenWrite=function(a,b,c){b||(b={});b=Wq(a,b);Bm()||(this.h=!1);dq.prototype.sendThenWrite.call(this,a,b,c)};
Rq.prototype.sendAndWrite=function(a,b){b||(b={});b=Wq(a,b);Bm()||(this.h=!1);dq.prototype.sendAndWrite.call(this,a,b)};
Rq.prototype.awaitInitialization=function(){return this.j.promise};
function Vq(a){var b;z(function(c){if(!a.X)throw b=Ln("clearSWHealthLogsDb"),b;return c.return(Dq(a.X).catch(function(d){a.handleError(d)}))})}
function Sq(a,b,c,d){d=void 0===d?!1:d;b=U("web_fp_via_jspb")?Object.assign({},b):b;U("use_cfr_monitor")&&Xq(a,b);if(U("use_request_time_ms_header"))b.headers&&rl(a)&&(b.headers["X-Goog-Request-Time"]=JSON.stringify(Math.round(W())));else{var e;if(null==(e=b.postParams)?0:e.requestTimeMs)b.postParams.requestTimeMs=Math.round(W())}if(c&&0===Object.keys(b).length){var f=void 0===f?"":f;var g=void 0===g?!1:g;var h=void 0===h?!1:h;if(a)if(f)Fl(a,void 0,"POST",f,void 0);else if(T("USE_NET_AJAX_FOR_PING_TRANSPORT",
!1)||h)Fl(a,void 0,"GET","",void 0,void 0,g,h);else{b:{try{var k=new cb({url:a});if(k.j&&k.i||k.l){var l=mc(nc(5,a)),n;if(!(n=!l||!l.endsWith("/aclk"))){var p=a.search(vc),r=uc(a,0,"ri",p);if(0>r)var t=null;else{var v=a.indexOf("&",r);if(0>v||v>p)v=p;t=decodeURIComponent(a.slice(r+3,-1!==v?v:0).replace(/\+/g," "))}n="1"!==t}var w=!n;break b}}catch(F){}w=!1}if(w){b:{try{if(window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,"")){var C=!0;break b}}catch(F){}C=!1}c=C?!0:!1}else c=
!1;c||Gq(a)}}else b.compress?b.postBody?("string"!==typeof b.postBody&&(b.postBody=JSON.stringify(b.postBody)),Tp(a,b.postBody,b,Jl,d)):Tp(a,JSON.stringify(b.postParams),b,Il,d):Jl(a,b)}
function Wq(a,b){U("use_event_time_ms_header")&&rl(a)&&(b.headers||(b.headers={}),b.headers["X-Goog-Event-Time"]=JSON.stringify(Math.round(W())));return b}
function Xq(a,b){var c=b.onError?b.onError:function(){};
b.onError=function(e,f){Lq().requestComplete(a,!1);c(e,f)};
var d=b.onSuccess?b.onSuccess:function(){};
b.onSuccess=function(e,f){Lq().requestComplete(a,!0);d(e,f)}}
function Tq(){return"www.youtube-nocookie.com"!==oc(document.location.toString())}
;var Yq=!1,Zq=B.ytNetworklessLoggingInitializationOptions||{isNwlInitialized:Yq};D("ytNetworklessLoggingInitializationOptions",Zq);function $q(){var a;z(function(b){if(1==b.h)return b.yield(Ho(),2);a=b.i;if(!a||!Bm()&&!U("nwl_init_require_datasync_id_killswitch")||!Tq())return b.B(0);Yq=!0;Zq.isNwlInitialized=Yq;return b.yield(Uq().awaitInitialization(),0)})}
;function ar(a){var b=this;this.config_=null;a?this.config_=a:ip()&&(this.config_=jp());Em(function(){bq(b)},5E3)}
ar.prototype.isReady=function(){!this.config_&&ip()&&(this.config_=jp());return!!this.config_};
function cq(a,b,c,d){function e(v){v=void 0===v?!1:v;var w;if(d.retry&&"www.youtube-nocookie.com"!=h&&(v||U("skip_ls_gel_retry")||"application/json"!==g.headers["Content-Type"]||(w=$p(b,c,l,k)),w)){var C=g.onSuccess,F=g.onFetchSuccess;g.onSuccess=function(S,da){aq(w);C(S,da)};
c.onFetchSuccess=function(S,da){aq(w);F(S,da)}}try{if(v&&d.retry&&!d.networklessOptions.bypassNetworkless)g.method="POST",d.networklessOptions.writeThenSend?Uq().writeThenSend(t,g):Uq().sendAndWrite(t,g);
else if(d.compress){var K=!d.networklessOptions.writeThenSend;if(g.postBody){var N=g.postBody;"string"!==typeof N&&(N=JSON.stringify(g.postBody));Tp(t,N,g,Jl,K)}else Tp(t,JSON.stringify(g.postParams),g,Il,K)}else U("web_all_payloads_via_jspb")?Jl(t,g):Il(t,g)}catch(S){if("InvalidAccessError"===S.name)w&&(aq(w),w=0),hl(Error("An extension is blocking network request."));else throw S;}w&&Em(function(){bq(a)},5E3)}
!T("VISITOR_DATA")&&"visitor_id"!==b&&.01>Math.random()&&hl(new V("Missing VISITOR_DATA when sending innertube request.",b,c,d));if(!a.isReady()){var f=new V("innertube xhrclient not ready",b,c,d);gl(f);throw f;}var g={headers:d.headers||{},method:"POST",postParams:c,postBody:d.postBody,postBodyFormat:d.postBodyFormat||"JSON",onTimeout:function(){d.onTimeout()},
onFetchTimeout:d.onTimeout,onSuccess:function(v,w){if(d.onSuccess)d.onSuccess(w)},
onFetchSuccess:function(v){if(d.onSuccess)d.onSuccess(v)},
onError:function(v,w){if(d.onError)d.onError(w)},
onFetchError:function(v){if(d.onError)d.onError(v)},
timeout:d.timeout,withCredentials:!0,compress:d.compress};g.headers["Content-Type"]||(g.headers["Content-Type"]="application/json");var h="";(f=a.config_.ne)&&(h=f);var k=a.config_.pe||!1,l=lp(k,h,d);Object.assign(g.headers,l);(f=g.headers.Authorization)&&!h&&k&&(g.headers["x-origin"]=window.location.origin);var n="/youtubei/"+a.config_.innertubeApiVersion+"/"+b,p={alt:"json"},r=a.config_.oe&&f;r=r&&f.startsWith("Bearer");r||(p.key=a.config_.innertubeApiKey);var t=ql(""+h+n,p||{},!0);(E("ytNetworklessLoggingInitializationOptions")?
Zq.isNwlInitialized:Yq)?Fo().then(function(v){e(v)}):e(!1)}
;var br=0,cr=Yc?"webkit":Xc?"moz":Vc?"ms":Uc?"o":"";D("ytDomDomGetNextId",E("ytDomDomGetNextId")||function(){return++br});var dr={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function er(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.rotation=this.clientY=this.clientX=0;this.scale=1;this.changedTouches=this.touches=null;try{if(a=a||window.event){this.event=a;for(var b in a)b in dr||(this[b]=a[b]);this.scale=a.scale;this.rotation=a.rotation;var c=a.target||a.srcElement;c&&3==c.nodeType&&(c=c.parentNode);this.target=c;var d=a.relatedTarget;
if(d)try{d=d.nodeName?d:null}catch(e){d=null}else"mouseover"==this.type?d=a.fromElement:"mouseout"==this.type&&(d=a.toElement);this.relatedTarget=d;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.h=a.pageX;this.i=a.pageY}}catch(e){}}
function fr(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.h=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.i=a.clientY+b}}
er.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
er.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
er.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var Mb=B.ytEventsEventsListeners||{};D("ytEventsEventsListeners",Mb);var gr=B.ytEventsEventsCounter||{count:0};D("ytEventsEventsCounter",gr);
function hr(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return Lb(function(e){var f="boolean"===typeof e[4]&&e[4]==!!d,g=Ra(e[4])&&Ra(d)&&Qb(e[4],d);return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&(f||g)})}
function ir(a,b,c,d){d=void 0===d?{}:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=hr(a,b,c,d);if(e)return e;e=++gr.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(h){h=new er(h);if(!Hd(h.relatedTarget,function(k){return k==a}))return h.currentTarget=a,h.type=b,c.call(a,h)}:function(h){h=new er(h);
h.currentTarget=a;return c.call(a,h)};
g=fl(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),jr()||"boolean"===typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);Mb[e]=[a,b,c,g,d];return e}
function kr(a){a&&("string"==typeof a&&(a=[a]),Db(a,function(b){if(b in Mb){var c=Mb[b],d=c[0],e=c[1],f=c[3];c=c[4];d.removeEventListener?jr()||"boolean"===typeof c?d.removeEventListener(e,f,c):d.removeEventListener(e,f,!!c.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete Mb[b]}}))}
var jr=Cd(function(){var a=!1;try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});function lr(a){this.F=a;this.h=null;this.l=0;this.A=null;this.m=0;this.i=[];for(a=0;4>a;a++)this.i.push(0);this.j=0;this.W=ir(window,"mousemove",Xa(this.ba,this));a=Xa(this.K,this);"function"===typeof a&&(a=fl(a));this.da=window.setInterval(a,25)}
$a(lr,G);lr.prototype.ba=function(a){void 0===a.h&&fr(a);var b=a.h;void 0===a.i&&fr(a);this.h=new Dd(b,a.i)};
lr.prototype.K=function(){if(this.h){var a=W();if(0!=this.l){var b=this.A,c=this.h,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.l);this.i[this.j]=.5<Math.abs((d-this.m)/this.m)?1:0;for(c=b=0;4>c;c++)b+=this.i[c]||0;3<=b&&this.F();this.m=d}this.l=a;this.A=this.h;this.j=(this.j+1)%4}};
lr.prototype.U=function(){window.clearInterval(this.da);kr(this.W)};var mr={};
function nr(a){var b=void 0===a?{}:a;a=void 0===b.De?!1:b.De;b=void 0===b.Wd?!0:b.Wd;if(null==E("_lact",window)){var c=parseInt(T("LACT"),10);c=isFinite(c)?Date.now()-Math.max(c,0):-1;D("_lact",c,window);D("_fact",c,window);-1==c&&or();ir(document,"keydown",or);ir(document,"keyup",or);ir(document,"mousedown",or);ir(document,"mouseup",or);a?ir(window,"touchmove",function(){pr("touchmove",200)},{passive:!0}):(ir(window,"resize",function(){pr("resize",200)}),b&&ir(window,"scroll",function(){pr("scroll",200)}));
new lr(function(){pr("mouse",100)});
ir(document,"touchstart",or,{passive:!0});ir(document,"touchend",or,{passive:!0})}}
function pr(a,b){mr[a]||(mr[a]=!0,Pi.pa(function(){or();mr[a]=!1},b))}
function or(){null==E("_lact",window)&&nr();var a=Date.now();D("_lact",a,window);-1==E("_fact",window)&&D("_fact",a,window);(a=E("ytglobal.ytUtilActivityCallback_"))&&a()}
function qr(){var a=E("_lact",window);return null==a?-1:Math.max(Date.now()-a,0)}
;var ur=B.ytPubsubPubsubInstance||new M,vr=B.ytPubsubPubsubSubscribedKeys||{},wr=B.ytPubsubPubsubTopicToKeys||{},xr=B.ytPubsubPubsubIsSynchronous||{};function yr(a,b){var c=zr();if(c&&b){var d=c.subscribe(a,function(){function e(){vr[d]&&b.apply&&"function"==typeof b.apply&&b.apply(window,f)}
var f=arguments;try{xr[a]?e():xl(e,0)}catch(g){gl(g)}},void 0);
vr[d]=!0;wr[a]||(wr[a]=[]);wr[a].push(d);return d}return 0}
function Ar(a){var b=zr();b&&("number"===typeof a?a=[a]:"string"===typeof a&&(a=[parseInt(a,10)]),Db(a,function(c){b.unsubscribeByKey(c);delete vr[c]}))}
function Br(a,b){var c=zr();c&&c.publish.apply(c,arguments)}
function Cr(a){var b=zr();if(b)if(b.clear(a),a)Dr(a);else for(var c in wr)Dr(c)}
function zr(){return B.ytPubsubPubsubInstance}
function Dr(a){wr[a]&&(a=wr[a],Db(a,function(b){vr[b]&&delete vr[b]}),a.length=0)}
M.prototype.subscribe=M.prototype.subscribe;M.prototype.unsubscribeByKey=M.prototype.Bb;M.prototype.publish=M.prototype.Ya;M.prototype.clear=M.prototype.clear;D("ytPubsubPubsubInstance",ur);D("ytPubsubPubsubTopicToKeys",wr);D("ytPubsubPubsubIsSynchronous",xr);D("ytPubsubPubsubSubscribedKeys",vr);var Er=Symbol("injectionDeps");function Fr(a){this.name=a}
Fr.prototype.toString=function(){return"InjectionToken("+this.name+")"};
function Gr(a){this.key=a}
function Hr(){this.i=new Map;this.j=new Map;this.h=new Map}
function Ir(a,b){a.i.set(b.oc,b);var c=a.j.get(b.oc);if(c)try{c.Wg(a.resolve(b.oc))}catch(d){c.Ug(d)}}
Hr.prototype.resolve=function(a){return a instanceof Gr?Jr(this,a.key,[],!0):Jr(this,a,[])};
function Jr(a,b,c,d){d=void 0===d?!1:d;if(-1<c.indexOf(b))throw Error("Deps cycle for: "+b);if(a.h.has(b))return a.h.get(b);if(!a.i.has(b)){if(d)return;throw Error("No provider for: "+b);}d=a.i.get(b);c.push(b);if(void 0!==d.Dd)var e=d.Dd;else if(d.mf)e=d[Er]?Kr(a,d[Er],c):[],e=d.mf.apply(d,la(e));else if(d.Cd){e=d.Cd;var f=e[Er]?Kr(a,e[Er],c):[];e=new (Function.prototype.bind.apply(e,[null].concat(la(f))))}else throw Error("Could not resolve providers for: "+b);c.pop();d.Zg||a.h.set(b,e);return e}
function Kr(a,b,c){return b?b.map(function(d){return d instanceof Gr?Jr(a,d.key,c,!0):Jr(a,d,c)}):[]}
;var Lr;function Mr(){Lr||(Lr=new Hr);return Lr}
;var Nr=window;function Or(){var a,b;return"h5vcc"in Nr&&(null==(a=Nr.h5vcc.traceEvent)?0:a.traceBegin)&&(null==(b=Nr.h5vcc.traceEvent)?0:b.traceEnd)?1:"performance"in Nr&&Nr.performance.mark&&Nr.performance.measure?2:0}
function Pr(a){var b=Or();switch(b){case 1:Nr.h5vcc.traceEvent.traceBegin("YTLR",a);break;case 2:Nr.performance.mark(a+"-start");break;case 0:break;default:Xb(b,"unknown trace type")}}
function Qr(a){var b=Or();switch(b){case 1:Nr.h5vcc.traceEvent.traceEnd("YTLR",a);break;case 2:b=a+"-start";var c=a+"-end";Nr.performance.mark(c);Nr.performance.measure(a,b,c);break;case 0:break;default:Xb(b,"unknown trace type")}}
;var Rr=U("web_enable_lifecycle_monitoring")&&0!==Or(),Sr=U("web_enable_lifecycle_monitoring");function Tr(a){var b=this;var c=void 0===c?0:c;var d=void 0===d?jn():d;this.j=c;this.scheduler=d;this.i=new yi;this.h=a;for(a={cb:0};a.cb<this.h.length;a={lc:void 0,cb:a.cb},a.cb++)a.lc=this.h[a.cb],c=function(e){return function(){e.lc.Ac();b.h[e.cb].nc=!0;b.h.every(function(f){return!0===f.nc})&&b.i.resolve()}}(a),d=this.getPriority(a.lc),d=this.scheduler.ab(c,d),this.h[a.cb]=Object.assign({},a.lc,{Ac:c,
jobId:d})}
function Ur(a){var b=Array.from(a.h.keys()).sort(function(d,e){return a.getPriority(a.h[e])-a.getPriority(a.h[d])});
b=x(b);for(var c=b.next();!c.done;c=b.next())c=a.h[c.value],void 0===c.jobId||c.nc||(a.scheduler.qa(c.jobId),a.scheduler.ab(c.Ac,10))}
Tr.prototype.cancel=function(){for(var a=x(this.h),b=a.next();!b.done;b=a.next())b=b.value,void 0===b.jobId||b.nc||this.scheduler.qa(b.jobId),b.nc=!0;this.i.resolve()};
Tr.prototype.getPriority=function(a){var b;return null!=(b=a.priority)?b:this.j};function Vr(a){this.state=a;this.plugins=[];this.l=void 0;this.A={};Rr&&Pr(this.state)}
m=Vr.prototype;m.install=function(a){this.plugins.push(a);return this};
m.uninstall=function(){var a=this;A.apply(0,arguments).forEach(function(b){b=a.plugins.indexOf(b);-1<b&&a.plugins.splice(b,1)})};
m.transition=function(a,b){var c=this;Rr&&Qr(this.state);var d=this.transitions.find(function(f){return Array.isArray(f.from)?f.from.find(function(g){return g===c.state&&f.to===a}):f.from===c.state&&f.to===a});
if(d){this.j&&(Ur(this.j),this.j=void 0);Wr(this,a,b);this.state=a;Rr&&Pr(this.state);d=d.action.bind(this);var e=this.plugins.filter(function(f){return f[a]}).map(function(f){return f[a]});
d(Xr(this,e),b)}else throw Error("no transition specified from "+this.state+" to "+a);};
function Xr(a,b){var c=b.filter(function(e){return 10===Yr(a,e)}),d=b.filter(function(e){return 10!==Yr(a,e)});
return a.A.Yg?function(){var e=A.apply(0,arguments);return z(function(f){if(1==f.h)return f.yield(a.Ke.apply(a,[c].concat(la(e))),2);a.yd.apply(a,[d].concat(la(e)));f.h=0})}:function(){var e=A.apply(0,arguments);
a.Le.apply(a,[c].concat(la(e)));a.yd.apply(a,[d].concat(la(e)))}}
m.Le=function(a){for(var b=A.apply(1,arguments),c=jn(),d=x(a),e=d.next(),f={};!e.done;f={Lb:void 0},e=d.next())f.Lb=e.value,c.Db(function(g){return function(){Zr(g.Lb.name);g.Lb.callback.apply(g.Lb,la(b));$r(g.Lb.name)}}(f))};
m.Ke=function(a){var b=A.apply(1,arguments),c,d,e,f,g;return z(function(h){1==h.h&&(c=jn(),d=x(a),e=d.next(),f={});if(3!=h.h){if(e.done)return h.B(0);f.tb=e.value;f.Wb=void 0;g=function(k){return function(){Zr(k.tb.name);var l=k.tb.callback.apply(k.tb,la(b));"function"===typeof(null==l?void 0:l.then)?k.Wb=l.then(function(){$r(k.tb.name)}):$r(k.tb.name)}}(f);
c.Db(g);return f.Wb?h.yield(f.Wb,3):h.B(3)}f={tb:void 0,Wb:void 0};e=d.next();return h.B(2)})};
m.yd=function(a){var b=A.apply(1,arguments),c=this,d=a.map(function(e){return{Ac:function(){Zr(e.name);e.callback.apply(e,la(b));$r(e.name)},
priority:Yr(c,e)}});
d.length&&(this.j=new Tr(d))};
function Yr(a,b){var c,d;return null!=(d=null!=(c=a.l)?c:b.priority)?d:0}
function Zr(a){Rr&&a&&Pr(a)}
function $r(a){Rr&&a&&Qr(a)}
function Wr(a,b,c){Sr&&console.groupCollapsed&&console.groupEnd&&(console.groupCollapsed("["+a.constructor.name+"] '"+a.state+"' to '"+b+"'"),console.log("with message: ",c),console.groupEnd())}
fa.Object.defineProperties(Vr.prototype,{currentState:{configurable:!0,enumerable:!0,get:function(){return this.state}}});function as(a){Vr.call(this,void 0===a?"none":a);this.h=null;this.l=10;this.transitions=[{from:"none",to:"application_navigating",action:this.i},{from:"application_navigating",to:"none",action:this.v},{from:"application_navigating",to:"application_navigating",action:function(){}},
{from:"none",to:"none",action:function(){}}]}
var bs;y(as,Vr);as.prototype.i=function(a,b){var c=this;this.h=Em(function(){"application_navigating"===c.currentState&&c.transition("none")},5E3);
a(null==b?void 0:b.event)};
as.prototype.v=function(a,b){this.h&&(Pi.qa(this.h),this.h=null);a(null==b?void 0:b.event)};
function cs(){bs||(bs=new as);return bs}
;var ds=[];D("yt.logging.transport.getScrapedGelPayloads",function(){return ds});function es(){this.store={};this.h={}}
es.prototype.storePayload=function(a,b){a=gs(a);this.store[a]?this.store[a].push(b):(this.h={},this.store[a]=[b]);return a};
es.prototype.smartExtractMatchingEntries=function(a){if(!a.keys.length)return[];for(var b=hs(this,a.keys.splice(0,1)[0]),c=[],d=0;d<b.length;d++)this.store[b[d]]&&a.sizeLimit&&(this.store[b[d]].length<=a.sizeLimit?(c.push.apply(c,la(this.store[b[d]])),delete this.store[b[d]]):c.push.apply(c,la(this.store[b[d]].splice(0,a.sizeLimit))));(null==a?0:a.sizeLimit)&&c.length<(null==a?void 0:a.sizeLimit)&&(a.sizeLimit-=c.length,c.push.apply(c,la(this.smartExtractMatchingEntries(a))));return c};
es.prototype.extractMatchingEntries=function(a){a=hs(this,a);for(var b=[],c=0;c<a.length;c++)this.store[a[c]]&&(b.push.apply(b,la(this.store[a[c]])),delete this.store[a[c]]);return b};
es.prototype.getSequenceCount=function(a){a=hs(this,a);for(var b=0,c=0;c<a.length;c++){var d=void 0;b+=(null==(d=this.store[a[c]])?void 0:d.length)||0}return b};
function hs(a,b){var c=gs(b);if(a.h[c])return a.h[c];var d=Object.keys(a.store)||[];if(1>=d.length&&gs(b)===d[0])return d;for(var e=[],f=0;f<d.length;f++){var g=d[f].split("/");if(is(b.auth,g[0])){var h=b.isJspb;is(void 0===h?"undefined":h?"true":"false",g[1])&&is(b.cttAuthInfo,g[2])&&(h=b.tier,h=void 0===h?"undefined":JSON.stringify(h),is(h,g[3])&&e.push(d[f]))}}return a.h[c]=e}
function is(a,b){return void 0===a||"undefined"===a?!0:a===b}
es.prototype.getSequenceCount=es.prototype.getSequenceCount;es.prototype.extractMatchingEntries=es.prototype.extractMatchingEntries;es.prototype.smartExtractMatchingEntries=es.prototype.smartExtractMatchingEntries;es.prototype.storePayload=es.prototype.storePayload;function gs(a){return[void 0===a.auth?"undefined":a.auth,void 0===a.isJspb?"undefined":a.isJspb,void 0===a.cttAuthInfo?"undefined":a.cttAuthInfo,void 0===a.tier?"undefined":a.tier].join("/")}
;function js(a,b){if(a)return a[b.name]}
;var ks=Al("initial_gel_batch_timeout",2E3),ls=Al("gel_queue_timeout_max_ms",6E4),ms=Math.pow(2,16)-1,ns=Al("gel_min_batch_size",5),ps=void 0;function qs(){this.l=this.h=this.i=0;this.j=!1}
var rs=new qs,ss=new qs,ts=new qs,us=new qs,vs,ws=!0,xs=B.ytLoggingTransportTokensToCttTargetIds_||{};D("ytLoggingTransportTokensToCttTargetIds_",xs);var ys={};function zs(){var a=E("yt.logging.ims");a||(a=new es,D("yt.logging.ims",a));return a}
function As(a,b){if("log_event"===a.endpoint){Bs();var c=Cs(a),d=Ds(a.payload)||"";a:{if(U("enable_web_tiered_gel")){var e=yq[d||""];var f,g,h,k=null==Mr().resolve(new Gr(dp))?void 0:null==(f=ep())?void 0:null==(g=f.loggingHotConfig)?void 0:null==(h=g.eventLoggingConfig)?void 0:h.payloadPolicies;if(k)for(f=0;f<k.length;f++)if(k[f].payloadNumber===e){e=k[f];break a}}e=void 0}k=200;if(e){if(!1===e.enabled&&!U("web_payload_policy_disabled_killswitch"))return;k=Es(e.tier);if(400===k){Fs(a,b);return}}ys[c]=
!0;e={cttAuthInfo:c,isJspb:!1,tier:k};zs().storePayload(e,a.payload);Gs(b,c,e,"gelDebuggingEvent"===d)}}
function Gs(a,b,c,d){function e(){Hs({writeThenSend:!0},U("flush_only_full_queue")?b:void 0,f,c.tier)}
var f=!1;f=void 0===f?!1:f;d=void 0===d?!1:d;a&&(ps=new a);a=Al("tvhtml5_logging_max_batch_ads_fork")||Al("web_logging_max_batch")||100;var g=W(),h=Is(f,c.tier),k=h.l;d&&(h.j=!0);d=0;c&&(d=zs().getSequenceCount(c));1E3<=d?e():d>=a?vs||(vs=Js(function(){e();vs=void 0},0)):10<=g-k&&(Ks(f,c.tier),h.l=g)}
function Fs(a,b){if("log_event"===a.endpoint){Bs();var c=Cs(a),d=new Map;d.set(c,[a.payload]);var e=Ds(a.payload)||"";b&&(ps=new b);return new Ud(function(f,g){ps&&ps.isReady()?Ls(d,ps,f,g,{bypassNetworkless:!0},!0,"gelDebuggingEvent"===e):f()})}}
function Cs(a){var b="";if(a.dangerousLogToVisitorSession)b="visitorOnlyApprovedKey";else if(a.cttAuthInfo){b=a.cttAuthInfo;var c={};b.videoId?c.videoId=b.videoId:b.playlistId&&(c.playlistId=b.playlistId);xs[a.cttAuthInfo.token]=c;b=a.cttAuthInfo.token}return b}
function Hs(a,b,c,d){a=void 0===a?{}:a;c=void 0===c?!1:c;new Ud(function(e,f){var g=Is(c,d),h=g.j;g.j=!1;Ms(g.i);Ms(g.h);g.h=0;ps&&ps.isReady()?void 0===d&&U("enable_web_tiered_gel")?Ns(e,f,a,b,c,300,h):Ns(e,f,a,b,c,d,h):(Ks(c,d),e())})}
function Ns(a,b,c,d,e,f,g){var h=ps;c=void 0===c?{}:c;e=void 0===e?!1:e;f=void 0===f?200:f;g=void 0===g?!1:g;var k=new Map,l={isJspb:e,cttAuthInfo:d,tier:f};e={isJspb:e,cttAuthInfo:d};if(void 0!==d)f=U("enable_web_tiered_gel")?zs().smartExtractMatchingEntries({keys:[l,e],sizeLimit:1E3}):zs().extractMatchingEntries(e),k.set(d,f);else for(d=x(Object.keys(ys)),l=d.next();!l.done;l=d.next())l=l.value,e=U("enable_web_tiered_gel")?zs().smartExtractMatchingEntries({keys:[{isJspb:!1,cttAuthInfo:l,tier:f},
{isJspb:!1,cttAuthInfo:l}],sizeLimit:1E3}):zs().extractMatchingEntries({isJspb:!1,cttAuthInfo:l}),0<e.length&&k.set(l,e),(U("web_fp_via_jspb_and_json")&&c.writeThenSend||!U("web_fp_via_jspb_and_json"))&&delete ys[l];Ls(k,h,a,b,c,!1,g)}
function Ks(a,b){function c(){Hs({writeThenSend:!0},void 0,a,b)}
a=void 0===a?!1:a;b=void 0===b?200:b;var d=Is(a,b),e=d===us||d===ts?5E3:ls;U("web_gel_timeout_cap")&&!d.h&&(e=Js(function(){c()},e),d.h=e);
Ms(d.i);e=T("LOGGING_BATCH_TIMEOUT",Al("web_gel_debounce_ms",1E4));U("shorten_initial_gel_batch_timeout")&&ws&&(e=ks);e=Js(function(){0<Al("gel_min_batch_size")?zs().getSequenceCount({cttAuthInfo:void 0,isJspb:a,tier:b})>=ns&&c():c()},e);
d.i=e}
function Ls(a,b,c,d,e,f,g){e=void 0===e?{}:e;var h=Math.round(W()),k=a.size,l=(void 0===g?0:g)&&U("vss_through_gel_video_stats")?"video_stats":"log_event";a=x(a);var n=a.next();for(g={};!n.done;g={Gc:void 0,batchRequest:void 0,dangerousLogToVisitorSession:void 0,Jc:void 0,Ic:void 0},n=a.next()){var p=x(n.value);n=p.next().value;p=p.next().value;g.batchRequest=Sb({context:kp(b.config_||jp())});if(!Qa(p)&&!U("throw_err_when_logevent_malformed_killswitch")){d();break}g.batchRequest.events=p;(p=xs[n])&&
Os(g.batchRequest,n,p);delete xs[n];g.dangerousLogToVisitorSession="visitorOnlyApprovedKey"===n;Ps(g.batchRequest,h,g.dangerousLogToVisitorSession);U("always_send_and_write")&&(e.writeThenSend=!1);g.Jc=function(r){U("start_client_gcf")&&Pi.pa(function(){return z(function(t){return t.yield(Qs(r),0)})});
k--;k||c()};
g.Gc=0;g.Ic=function(r){return function(){r.Gc++;if(e.bypassNetworkless&&1===r.Gc)try{cq(b,l,r.batchRequest,Rs({writeThenSend:!0},r.dangerousLogToVisitorSession,r.Jc,r.Ic,f)),ws=!1}catch(t){gl(t),d()}k--;k||c()}}(g);
try{cq(b,l,g.batchRequest,Rs(e,g.dangerousLogToVisitorSession,g.Jc,g.Ic,f)),ws=!1}catch(r){gl(r),d()}}}
function Rs(a,b,c,d,e){a={retry:!0,onSuccess:c,onError:d,networklessOptions:a,dangerousLogToVisitorSession:b,Eg:!!e,headers:{},postBodyFormat:"",postBody:"",compress:U("compress_gel")||U("compress_gel_lr")};Ss()&&(a.headers["X-Goog-Request-Time"]=JSON.stringify(Math.round(W())));return a}
function Ps(a,b,c){Ss()||(a.requestTimeMs=String(b));U("unsplit_gel_payloads_in_logs")&&(a.unsplitGelPayloadsInLogs=!0);!c&&(b=T("EVENT_ID"))&&((c=T("BATCH_CLIENT_COUNTER")||0)||(c=Math.floor(Math.random()*ms/2)),c++,c>ms&&(c=1),bl("BATCH_CLIENT_COUNTER",c),a.serializedClientEventId={serializedEventId:b,clientCounter:String(c)})}
function Os(a,b,c){if(c.videoId)var d="VIDEO";else if(c.playlistId)d="PLAYLIST";else return;a.credentialTransferTokenTargetId=c;a.context=a.context||{};a.context.user=a.context.user||{};a.context.user.credentialTransferTokens=[{token:b,scope:d}]}
function Bs(){var a;(a=E("yt.logging.transport.enableScrapingForTest"))||(a=zl("il_payload_scraping"),a="enable_il_payload_scraping"!==(void 0!==a?String(a):""));a||(ds=[],D("yt.logging.transport.enableScrapingForTest",!0),D("yt.logging.transport.scrapedPayloadsForTesting",ds),D("yt.logging.transport.payloadToScrape","visualElementShown visualElementHidden visualElementAttached screenCreated visualElementGestured visualElementStateChanged".split(" ")),D("yt.logging.transport.getScrapedPayloadFromClientEventsFunction"),
D("yt.logging.transport.scrapeClientEvent",!0))}
function Ss(){return U("use_request_time_ms_header")||U("lr_use_request_time_ms_header")}
function Js(a,b){return!1===U("transport_use_scheduler")?xl(a,b):U("logging_avoid_blocking_during_navigation")||U("lr_logging_avoid_blocking_during_navigation")?Em(function(){if("none"===cs().currentState)a();else{var c={};cs().install((c.none={callback:a},c))}},b):Em(a,b)}
function Ms(a){U("transport_use_scheduler")?Pi.qa(a):window.clearTimeout(a)}
function Qs(a){var b,c,d,e,f,g,h,k,l,n;return z(function(p){return 1==p.h?(d=null==(b=a)?void 0:null==(c=b.responseContext)?void 0:c.globalConfigGroup,e=js(d,Hk),g=null==(f=d)?void 0:f.hotHashData,h=js(d,Gk),l=null==(k=d)?void 0:k.coldHashData,(n=Mr().resolve(new Gr(dp)))?g?e?p.yield(fp(n,g,e),2):p.yield(fp(n,g),2):p.B(2):p.return()):l?h?p.yield(gp(n,l,h),0):p.yield(gp(n,l),0):p.B(0)})}
function Is(a,b){b=void 0===b?200:b;return a?300===b?us:ss:300===b?ts:rs}
function Ds(a){a=Object.keys(a);a=x(a);for(var b=a.next();!b.done;b=a.next())if(b=b.value,yq[b])return b}
function Es(a){switch(a){case "DELAYED_EVENT_TIER_UNSPECIFIED":return 0;case "DELAYED_EVENT_TIER_DEFAULT":return 100;case "DELAYED_EVENT_TIER_DISPATCH_TO_EMPTY":return 200;case "DELAYED_EVENT_TIER_FAST":return 300;case "DELAYED_EVENT_TIER_IMMEDIATE":return 400;default:return 200}}
;var Ts=B.ytLoggingGelSequenceIdObj_||{};D("ytLoggingGelSequenceIdObj_",Ts);
function Us(a,b,c,d){d=void 0===d?{}:d;var e={},f=Math.round(d.timestamp||W());e.eventTimeMs=f<Number.MAX_SAFE_INTEGER?f:0;e[a]=b;a=qr();e.context={lastActivityMs:String(d.timestamp||!isFinite(a)?-1:a)};d.sequenceGroup&&!U("web_gel_sequence_info_killswitch")&&(a=e.context,b=d.sequenceGroup,Ts[b]=b in Ts?Ts[b]+1:0,a.sequence={index:Ts[b],groupKey:b},d.endOfSequence&&delete Ts[d.sequenceGroup]);(d.sendIsolatedPayload?Fs:As)({endpoint:"log_event",payload:e,cttAuthInfo:d.cttAuthInfo,dangerousLogToVisitorSession:d.dangerousLogToVisitorSession},
c)}
;function tn(a,b,c){c=void 0===c?{}:c;var d=ar;T("ytLoggingEventsDefaultDisabled",!1)&&ar===ar&&(d=null);U("web_all_payloads_via_jspb")&&!c.timestamp&&(c.lact=qr(),c.timestamp=W());Us(a,b,d,c)}
;D("ytLoggingGelSequenceIdObj_",B.ytLoggingGelSequenceIdObj_||{});var Vs=new Set,Ws=0,Xs=0,Ys=0,Zs=[],$s=["PhantomJS","Googlebot","TO STOP THIS SECURITY SCAN go/scan"];function sn(a){at(a)}
function bt(a){at(a,"WARNING")}
function ct(a){a instanceof Error?at(a):(a=Ra(a)?JSON.stringify(a):String(a),a=new V(a),a.name="RejectedPromiseError",bt(a))}
function at(a,b,c,d,e,f,g,h){f=void 0===f?{}:f;f.name=c||T("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||T("INNERTUBE_CONTEXT_CLIENT_VERSION");c=f;b=void 0===b?"ERROR":b;g=void 0===g?!1:g;b=void 0===b?"ERROR":b;g=void 0===g?!1:g;if(a&&(a.hasOwnProperty("level")&&a.level&&(b=a.level),U("console_log_js_exceptions")&&(d=[],d.push("Name: "+a.name),d.push("Message: "+a.message),a.hasOwnProperty("params")&&d.push("Error Params: "+JSON.stringify(a.params)),a.hasOwnProperty("args")&&d.push("Error args: "+
JSON.stringify(a.args)),d.push("File name: "+a.fileName),d.push("Stacktrace: "+a.stack),d=d.join("\n"),window.console.log(d,a)),!(5<=Ws))){d=Zs;var k=fc(a);e=k.message||"Unknown Error";f=k.name||"UnknownError";var l=k.stack||a.i||"Not available";if(l.startsWith(f+": "+e)){var n=l.split("\n");n.shift();l=n.join("\n")}n=k.lineNumber||"Not available";k=k.fileName||"Not available";var p=0;if(a.hasOwnProperty("args")&&a.args&&a.args.length)for(var r=0;r<a.args.length&&!(p=am(a.args[r],"params."+r,c,p),
500<=p);r++);else if(a.hasOwnProperty("params")&&a.params){var t=a.params;if("object"===typeof a.params)for(r in t){if(t[r]){var v="params."+r,w=cm(t[r]);c[v]=w;p+=v.length+w.length;if(500<p)break}}else c.params=cm(t)}if(d.length)for(r=0;r<d.length&&!(p=am(d[r],"params.context."+r,c,p),500<=p);r++);navigator.vendor&&!c.hasOwnProperty("vendor")&&(c["device.vendor"]=navigator.vendor);r={message:e,name:f,lineNumber:n,fileName:k,stack:l,params:c,sampleWeight:1};c=Number(a.columnNumber);isNaN(c)||(r.lineNumber=
r.lineNumber+":"+c);if("IGNORED"===a.level)a=0;else a:{a=Xl();c=x(a.Va);for(d=c.next();!d.done;d=c.next())if(d=d.value,r.message&&r.message.match(d.Qg)){a=d.weight;break a}a=x(a.Sa);for(c=a.next();!c.done;c=a.next())if(c=c.value,c.callback(r)){a=c.weight;break a}a=1}r.sampleWeight=a;a=x(Sl);for(c=a.next();!c.done;c=a.next())if(c=c.value,c.kc[r.name])for(e=x(c.kc[r.name]),d=e.next();!d.done;d=e.next())if(f=d.value,d=r.message.match(f.regexp)){r.params["params.error.original"]=d[0];e=f.groups;f={};
for(n=0;n<e.length;n++)f[e[n]]=d[n+1],r.params["params.error."+e[n]]=d[n+1];r.message=c.Ec(f);break}r.params||(r.params={});a=Xl();r.params["params.errorServiceSignature"]="msg="+a.Va.length+"&cb="+a.Sa.length;r.params["params.serviceWorker"]="false";B.document&&B.document.querySelectorAll&&(r.params["params.fscripts"]=String(document.querySelectorAll("script:not([nonce])").length));ib("sample").constructor!==gb&&(r.params["params.fconst"]="true");window.yterr&&"function"===typeof window.yterr&&window.yterr(r);
if(0!==r.sampleWeight&&!Vs.has(r.message)){if(g&&U("web_enable_error_204"))dt(void 0===b?"ERROR":b,r);else{b=void 0===b?"ERROR":b;"ERROR"===b?(Yl.Ya("handleError",r),U("record_app_crashed_web")&&0===Ys&&1===r.sampleWeight&&(Ys++,g={appCrashType:"APP_CRASH_TYPE_BREAKPAD"},U("report_client_error_with_app_crash_ks")||(g.systemHealth={crashData:{clientError:{logMessage:{message:r.message}}}}),tn("appCrashed",g)),Xs++):"WARNING"===b&&Yl.Ya("handleWarning",r);if(U("kevlar_gel_error_routing")){g=b;h=void 0===
h?{}:h;b:{a=x($s);for(c=a.next();!c.done;c=a.next())if(zn(c.value.toLowerCase())){a=!0;break b}a=!1}if(a)h=void 0;else{c={stackTrace:r.stack};r.fileName&&(c.filename=r.fileName);a=r.lineNumber&&r.lineNumber.split?r.lineNumber.split(":"):[];0!==a.length&&(1!==a.length||isNaN(Number(a[0]))?2!==a.length||isNaN(Number(a[0]))||isNaN(Number(a[1]))||(c.lineNumber=Number(a[0]),c.columnNumber=Number(a[1])):c.lineNumber=Number(a[0]));a={level:"ERROR_LEVEL_UNKNOWN",message:r.message,errorClassName:r.name,sampleWeight:r.sampleWeight};
"ERROR"===g?a.level="ERROR_LEVEL_ERROR":"WARNING"===g&&(a.level="ERROR_LEVEL_WARNNING");c={isObfuscated:!0,browserStackInfo:c};h.pageUrl=window.location.href;h.kvPairs=[];T("FEXP_EXPERIMENTS")&&(h.experimentIds=T("FEXP_EXPERIMENTS"));d=T("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS");if(!cl("web_disable_gel_stp_ecatcher_killswitch")&&d)for(e=x(Object.keys(d)),f=e.next();!f.done;f=e.next())f=f.value,h.kvPairs.push({key:f,value:String(d[f])});if(d=r.params)for(e=x(Object.keys(d)),f=e.next();!f.done;f=e.next())f=
f.value,h.kvPairs.push({key:"client."+f,value:String(d[f])});d=T("SERVER_NAME");e=T("SERVER_VERSION");d&&e&&(h.kvPairs.push({key:"server.name",value:d}),h.kvPairs.push({key:"server.version",value:e}));h={errorMetadata:h,stackTrace:c,logMessage:a}}h&&(tn("clientError",h),("ERROR"===g||U("errors_flush_gel_always_killswitch"))&&Hs(void 0,void 0,!1))}U("suppress_error_204_logging")||dt(b,r)}try{Vs.add(r.message)}catch(C){}Ws++}}}
function dt(a,b){var c=b.params||{};a={urlParams:{a:"logerror",t:"jserror",type:b.name,msg:b.message.substr(0,250),line:b.lineNumber,level:a,"client.name":c.name},postParams:{url:T("PAGE_NAME",window.location.href),file:b.fileName},method:"POST"};c.version&&(a["client.version"]=c.version);if(a.postParams){b.stack&&(a.postParams.stack=b.stack);b=x(Object.keys(c));for(var d=b.next();!d.done;d=b.next())d=d.value,a.postParams["client."+d]=c[d];if(c=T("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS"))for(b=x(Object.keys(c)),
d=b.next();!d.done;d=b.next())d=d.value,a.postParams[d]=c[d];c=T("SERVER_NAME");b=T("SERVER_VERSION");c&&b&&(a.postParams["server.name"]=c,a.postParams["server.version"]=b)}Jl(T("ECATCHER_REPORT_HOST","")+"/error_204",a)}
;function et(){this.register=new Map}
function ft(a){a=x(a.register.values());for(var b=a.next();!b.done;b=a.next())b.value.Tg("ABORTED")}
et.prototype.clear=function(){ft(this);this.register.clear()};
var gt=new et;var ht=Date.now().toString();
function jt(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=Array(16);for(a=0;16>a;a++){b=Date.now();for(c=0;c<b%23;c++)d[a]=Math.random();d[a]=Math.floor(256*Math.random())}if(ht)for(a=1,b=0;b<ht.length;b++)d[a%16]=d[a%16]^d[(a-1)%16]/4^ht.charCodeAt(b),a++}a=[];for(b=0;b<d.length;b++)a.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(d[b]&63));
return a.join("")}
;var kt,lt=B.ytLoggingDocDocumentNonce_;lt||(lt=jt(),D("ytLoggingDocDocumentNonce_",lt));kt=lt;function mt(a){this.h=a}
m=mt.prototype;m.getAsJson=function(){var a={};void 0!==this.h.trackingParams?a.trackingParams=this.h.trackingParams:(a.veType=this.h.veType,void 0!==this.h.veCounter&&(a.veCounter=this.h.veCounter),void 0!==this.h.elementIndex&&(a.elementIndex=this.h.elementIndex));void 0!==this.h.dataElement&&(a.dataElement=this.h.dataElement.getAsJson());void 0!==this.h.youtubeData&&(a.youtubeData=this.h.youtubeData);this.h.isCounterfactual&&(a.isCounterfactual=!0);return a};
m.getAsJspb=function(){var a=new Ok;void 0!==this.h.trackingParams?a.setTrackingParams(this.h.trackingParams):(void 0!==this.h.veType&&J(a,2,Mf(this.h.veType)),void 0!==this.h.veCounter&&J(a,6,Mf(this.h.veCounter)),void 0!==this.h.elementIndex&&J(a,3,Mf(this.h.elementIndex)),this.h.isCounterfactual&&J(a,5,If(!0)));if(void 0!==this.h.dataElement){var b=this.h.dataElement.getAsJspb();Gg(a,Ok,7,b)}void 0!==this.h.youtubeData&&Gg(a,Ik,8,this.h.jspbYoutubeData);return a};
m.toString=function(){return JSON.stringify(this.getAsJson())};
m.isClientVe=function(){return!this.h.trackingParams&&!!this.h.veType};
m.getLoggingDirectives=function(){return this.h.loggingDirectives};function nt(a){return T("client-screen-nonce-store",{})[void 0===a?0:a]}
function ot(a,b){b=void 0===b?0:b;var c=T("client-screen-nonce-store");c||(c={},bl("client-screen-nonce-store",c));c[b]=a}
function pt(a){a=void 0===a?0:a;return 0===a?"ROOT_VE_TYPE":"ROOT_VE_TYPE."+a}
function qt(a){return T(pt(void 0===a?0:a))}
D("yt_logging_screen.getRootVeType",qt);function rt(){var a=T("csn-to-ctt-auth-info");a||(a={},bl("csn-to-ctt-auth-info",a));return a}
function st(){return Object.values(T("client-screen-nonce-store",{})).filter(function(a){return void 0!==a})}
function tt(a){a=nt(void 0===a?0:a);if(!a&&!T("USE_CSN_FALLBACK",!0))return null;a||(a="UNDEFINED_CSN");return a?a:null}
D("yt_logging_screen.getCurrentCsn",tt);function ut(a,b,c){var d=rt();(c=tt(c))&&delete d[c];b&&(d[a]=b)}
function vt(a){return rt()[a]}
D("yt_logging_screen.getCttAuthInfo",vt);D("yt_logging_screen.setCurrentScreen",function(a,b,c,d){c=void 0===c?0:c;if(a!==nt(c)||b!==T(pt(c)))if(ut(a,d,c),ot(a,c),bl(pt(c),b),b=function(){setTimeout(function(){a&&tn("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:kt,clientScreenNonce:a})},0)},"requestAnimationFrame"in window)try{window.requestAnimationFrame(b)}catch(e){b()}else b()});function wt(){var a=Rb(xt),b;return(new Ud(function(c,d){a.onSuccess=function(e){wl(e)?c(new zt(e)):d(new At("Request failed, status="+(e&&"status"in e?e.status:-1),"net.badstatus",e))};
a.onError=function(e){d(new At("Unknown request error","net.unknown",e))};
a.onTimeout=function(e){d(new At("Request timed out","net.timeout",e))};
b=Jl("//googleads.g.doubleclick.net/pagead/id",a)})).qc(function(c){if(c instanceof ae){var d;
null==(d=b)||d.abort()}return Zd(c)})}
function At(a,b,c){bb.call(this,a+", errorCode="+b);this.errorCode=b;this.xhr=c;this.name="PromiseAjaxError"}
y(At,bb);function zt(a){this.xhr=a}
;function Bt(){this.h=0;this.i=null}
Bt.prototype.then=function(a,b,c){return 1===this.h&&a?(a=a.call(c,this.i))&&"function"===typeof a.then?a:Ct(a):2===this.h&&b?(a=b.call(c,this.i))&&"function"===typeof a.then?a:Dt(a):this};
Bt.prototype.getValue=function(){return this.i};
Bt.prototype.isRejected=function(){return 2==this.h};
Bt.prototype.$goog_Thenable=!0;function Dt(a){var b=new Bt;a=void 0===a?null:a;b.h=2;b.i=void 0===a?null:a;return b}
function Ct(a){var b=new Bt;a=void 0===a?null:a;b.h=1;b.i=void 0===a?null:a;return b}
;function Et(a,b){var c=void 0===c?{}:c;a={method:void 0===b?"POST":b,mode:rl(a)?"same-origin":"cors",credentials:rl(a)?"same-origin":"include"};b={};for(var d=x(Object.keys(c)),e=d.next();!e.done;e=d.next())e=e.value,c[e]&&(b[e]=c[e]);0<Object.keys(b).length&&(a.headers=b);return a}
;function Ft(){return mh()||(De||Ee)&&zn("applewebkit")&&!zn("version")&&(!zn("safari")||zn("gsa/"))||Zc&&zn("version/")?!0:T("EOM_VISITOR_DATA")?!1:!0}
;function Gt(a){a:{var b="EMBEDDED_PLAYER_MODE_UNKNOWN";window.location.hostname.includes("youtubeeducation.com")&&(b="EMBEDDED_PLAYER_MODE_PFL");var c=a.raw_embedded_player_response;if(!c&&(a=a.embedded_player_response))try{c=JSON.parse(a)}catch(e){break a}if(c)b:for(var d in Mk)if(Mk[d]==c.embeddedPlayerMode){b=Mk[d];break b}}return"EMBEDDED_PLAYER_MODE_PFL"===b}
;function Ht(a){bb.call(this,a.message||a.description||a.name);this.isMissing=a instanceof It;this.isTimeout=a instanceof At&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof ae}
y(Ht,bb);Ht.prototype.name="BiscottiError";function It(){bb.call(this,"Biscotti ID is missing from server")}
y(It,bb);It.prototype.name="BiscottiMissingError";var xt={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},Jt=null;function Kt(){if(U("disable_biscotti_fetch_entirely_for_all_web_clients"))return Error("Biscotti id fetching has been disabled entirely.");if(!Ft())return Error("User has not consented - not fetching biscotti id.");var a=T("PLAYER_VARS",{});if("1"==Pb(a))return Error("Biscotti ID is not available in private embed mode");if(Gt(a))return Error("Biscotti id fetching has been disabled for pfl.")}
function Vk(){var a=Kt();if(void 0!==a)return Zd(a);Jt||(Jt=wt().then(Lt).qc(function(b){return Mt(2,b)}));
return Jt}
function Lt(a){a=a.xhr.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new It;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new It;a=a.id;Wk(a);Jt=Ct(a);Nt(18E5,2);return a}
function Mt(a,b){b=new Ht(b);Wk("");Jt=Dt(b);0<a&&Nt(12E4,a-1);throw b;}
function Nt(a,b){xl(function(){wt().then(Lt,function(c){return Mt(b,c)}).qc(Bd)},a)}
function Ot(){try{var a=E("yt.ads.biscotti.getId_");return a?a():Vk()}catch(b){return Zd(b)}}
;var Bb=ja(["data-"]);function Pt(a){a&&(a.dataset?a.dataset[Qt()]="true":Wb(a))}
function Rt(a){return a?a.dataset?a.dataset[Qt()]:a.getAttribute("data-loaded"):null}
var St={};function Qt(){return St.loaded||(St.loaded="loaded".replace(/\-([a-z])/g,function(a,b){return b.toUpperCase()}))}
;function Tt(a){a=a||{};var b={},c={};this.url=a.url||"";this.args=a.args||Rb(b);this.assets=a.assets||{};this.attrs=a.attrs||Rb(c);this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
Tt.prototype.clone=function(){var a=new Tt,b;for(b in this)if(this.hasOwnProperty(b)){var c=this[b];"object"==Pa(c)?a[b]=Rb(c):a[b]=c}return a};var Ut=["share/get_web_player_share_panel"],Vt=["feedback"],Wt=["notification/modify_channel_preference"],Xt=["browse/edit_playlist"],Yt=["subscription/subscribe"],Zt=["subscription/unsubscribe"];var $t=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};D("yt.msgs_",$t);function au(a){Xk($t,arguments)}
;function bu(a,b,c){cu(a,b,void 0===c?null:c)}
function du(a){a=eu(a);var b=document.getElementById(a);b&&(Cr(a),b.parentNode.removeChild(b))}
function fu(a,b){a&&b&&(a=""+Sa(b),(a=gu[a])&&Ar(a))}
function cu(a,b,c){c=void 0===c?null:c;var d=eu(a),e=document.getElementById(d),f=e&&Rt(e),g=e&&!f;f?b&&b():(b&&(f=yr(d,b),b=""+Sa(b),gu[b]=f),g||(e=hu(a,d,function(){Rt(e)||(Pt(e),Br(d),xl(function(){Cr(d)},0))},c)))}
function hu(a,b,c,d){d=void 0===d?null:d;var e=Gd("SCRIPT");e.id=b;e.onload=function(){c&&setTimeout(c,0)};
e.onreadystatechange=function(){switch(e.readyState){case "loaded":case "complete":e.onload()}};
d&&e.setAttribute("nonce",d);dc(e,Ek(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(e,a.firstChild);return e}
function eu(a){var b=document.createElement("a");zb(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+kc(a)}
var gu={};function iu(a){var b=ju(a),c=document.getElementById(b),d=c&&Rt(c);d||c&&!d||(c=ku(a,b,function(){if(!Rt(c)){Pt(c);Br(b);var e=Ya(Cr,b);xl(e,0)}}))}
function ku(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Ek(a);Zb(d,a);(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function ju(a){var b=Gd("A");zb(b,new sb(a));a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+kc(a)}
;function lu(a){var b=A.apply(1,arguments);if(!mu(a)||b.some(function(d){return!mu(d)}))throw Error("Only objects may be merged.");
b=x(b);for(var c=b.next();!c.done;c=b.next())nu(a,c.value)}
function nu(a,b){for(var c in b)if(mu(b[c])){if(c in a&&!mu(a[c]))throw Error("Cannot merge an object into a non-object.");c in a||(a[c]={});nu(a[c],b[c])}else if(ou(b[c])){if(c in a&&!ou(a[c]))throw Error("Cannot merge an array into a non-array.");c in a||(a[c]=[]);pu(a[c],b[c])}else a[c]=b[c];return a}
function pu(a,b){b=x(b);for(var c=b.next();!c.done;c=b.next())c=c.value,mu(c)?a.push(nu({},c)):ou(c)?a.push(pu([],c)):a.push(c);return a}
function mu(a){return"object"===typeof a&&!Array.isArray(a)}
function ou(a){return"object"===typeof a&&Array.isArray(a)}
;function qu(a){a=void 0===a?!1:a;G.call(this);this.h=new M(a);Ec(this,this.h)}
$a(qu,G);qu.prototype.subscribe=function(a,b,c){return this.V?0:this.h.subscribe(a,b,c)};
qu.prototype.unsubscribe=function(a,b,c){return this.V?!1:this.h.unsubscribe(a,b,c)};
qu.prototype.l=function(a,b){this.V||this.h.Ya.apply(this.h,arguments)};var ru="absolute_experiments app conditional_experiments debugcss debugjs expflag forced_experiments pbj pbjreload sbb spf spfreload sr_bns_address sttick".split(" ");
function su(a,b){var c=void 0===c?!0:c;var d=T("VALID_SESSION_TEMPDATA_DOMAINS",[]),e=oc(window.location.href);e&&d.push(e);e=oc(a);if(0<=Cb(d,e)||!e&&0==a.lastIndexOf("/",0))if(d=document.createElement("a"),zb(d,a),a=d.href)if(a=pc(a),a=qc(a))if(c&&!b.csn&&(b.itct||b.ved)&&(b=Object.assign({csn:tt()},b)),f){var f=parseInt(f,10);isFinite(f)&&0<f&&tu(a,b,f)}else tu(a,b)}
function tu(a,b,c){a=uu(a);b=b?sc(b):"";c=c||5;Ft()&&jm(a,b,c)}
function uu(a){for(var b=x(ru),c=b.next();!c.done;c=b.next())a=xc(a,c.value);return"ST-"+kc(a).toString(36)}
;function vu(a){op.call(this,1,arguments);this.csn=a}
y(vu,op);var xp=new pp("screen-created",vu),wu=[],xu=0,yu=new Map,zu=new Map,Au=new Map;
function Bu(a,b,c,d,e){e=void 0===e?!1:e;for(var f=Cu({cttAuthInfo:vt(b)||void 0},b),g=x(d),h=g.next();!h.done;h=g.next()){h=h.value;var k=h.getAsJson();(Nb(k)||!k.trackingParams&&!k.veType)&&bt(Error("Child VE logged with no data"));if(U("no_client_ve_attach_unless_shown")){var l=Du(h,b);if(k.veType&&!zu.has(l)&&!Au.has(l)&&!e){if(!U("il_attach_cache_limit")||1E3>yu.size){yu.set(l,[a,b,c,h]);return}U("il_attach_cache_limit")&&1E3<yu.size&&bt(new V("IL Attach cache exceeded limit"))}h=Du(c,b);yu.has(h)?
Eu(c,b):Au.set(h,!0)}}d=d.filter(function(n){n.csn!==b?(n.csn=b,n=!0):n=!1;return n});
c={csn:b,parentVe:c.getAsJson(),childVes:Fb(d,function(n){return n.getAsJson()})};
"UNDEFINED_CSN"===b?Fu("visualElementAttached",f,c):a?Us("visualElementAttached",c,a,f):tn("visualElementAttached",c,f)}
function Fu(a,b,c){wu.push({Ce:a,payload:c,Mg:void 0,options:b});xu||(xu=yp())}
function zp(a){if(wu){for(var b=x(wu),c=b.next();!c.done;c=b.next())c=c.value,c.payload&&(c.payload.csn=a.csn,tn(c.Ce,c.payload,c.options));wu.length=0}xu=0}
function Du(a,b){return""+a.getAsJson().veType+a.getAsJson().veCounter+b}
function Eu(a,b){a=Du(a,b);yu.has(a)&&(b=yu.get(a)||[],Bu(b[0],b[1],b[2],[b[3]],!0),yu.delete(a))}
function Cu(a,b){U("log_sequence_info_on_gel_web")&&(a.sequenceGroup=b);return a}
;function Gu(){try{return!!self.localStorage}catch(a){return!1}}
;function Hu(a){a=a.match(/(.*)::.*::.*/);if(null!==a)return a[1]}
function Iu(a){if(Gu()){var b=Object.keys(window.localStorage);b=x(b);for(var c=b.next();!c.done;c=b.next()){c=c.value;var d=Hu(c);void 0===d||a.includes(d)||self.localStorage.removeItem(c)}}}
function Ju(){if(!Gu())return!1;var a=Cm(),b=Object.keys(window.localStorage);b=x(b);for(var c=b.next();!c.done;c=b.next())if(c=Hu(c.value),void 0!==c&&c!==a)return!0;return!1}
;function Ku(){var a=!1;try{a=!!window.sessionStorage.getItem("session_logininfo")}catch(b){a=!0}return("WEB"===T("INNERTUBE_CLIENT_NAME")||"WEB_CREATOR"===T("INNERTUBE_CLIENT_NAME"))&&a}
function Lu(a){if(T("LOGGED_IN",!0)&&Ku()){var b=T("VALID_SESSION_TEMPDATA_DOMAINS",[]);var c=oc(window.location.href);c&&b.push(c);c=oc(a);0<=Cb(b,c)||!c&&0==a.lastIndexOf("/",0)?(b=pc(a),(b=qc(b))?(b=uu(b),b=(b=km(b)||null)?ol(b):{}):b=null):b=null;null==b&&(b={});c=b;var d=void 0;Ku()?(d||(d=T("LOGIN_INFO")),d?(c.session_logininfo=d,c=!0):c=!1):c=!1;c&&su(a,b)}}
;function Mu(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=T("EVENT_ID");d&&(b.ei||(b.ei=d));b&&su(a,b);if(c)return!1;Lu(a);var e=void 0===e?{}:e;var f=void 0===f?"":f;var g=void 0===g?window:g;a=tc(a,e);Lu(a);f=a+f;var h=void 0===h?wb:h;a:if(h=void 0===h?wb:h,f instanceof sb)h=f;else{for(a=0;a<h.length;++a)if(b=h[a],b instanceof ub&&b.qe(f)){h=new sb(f);break a}h=void 0}g=g.location;h=yb(h||tb);void 0!==h&&(g.href=h);return!0}
;function Nu(a){if("1"!=Pb(T("PLAYER_VARS",{}))){a&&Uk();try{Ot().then(function(){},function(){}),xl(Nu,18E5)}catch(b){gl(b)}}}
;var Ou=new Map([["dark","USER_INTERFACE_THEME_DARK"],["light","USER_INTERFACE_THEME_LIGHT"]]);function Pu(){var a=void 0===a?window.location.href:a;if(U("kevlar_disable_theme_param"))return null;mc(nc(5,a));try{var b=pl(a).theme;return Ou.get(b)||null}catch(c){}return null}
;function Qu(){this.h={};if(this.i=mm()){var a=km("CONSISTENCY");a&&Ru(this,{encryptedTokenJarContents:a})}}
Qu.prototype.handleResponse=function(a,b){if(!b)throw Error("request needs to be passed into ConsistencyService");var c,d;b=(null==(c=b.Oa.context)?void 0:null==(d=c.request)?void 0:d.consistencyTokenJars)||[];var e;if(a=null==(e=a.responseContext)?void 0:e.consistencyTokenJar){e=x(b);for(c=e.next();!c.done;c=e.next())delete this.h[c.value.encryptedTokenJarContents];Ru(this,a)}};
function Ru(a,b){if(b.encryptedTokenJarContents&&(a.h[b.encryptedTokenJarContents]=b,"string"===typeof b.expirationSeconds)){var c=Number(b.expirationSeconds);setTimeout(function(){delete a.h[b.encryptedTokenJarContents]},1E3*c);
a.i&&jm("CONSISTENCY",b.encryptedTokenJarContents,c,void 0,!0)}}
;var Su=window.location.hostname.split(".").slice(-2).join(".");function Tu(){this.j=-1;var a=T("LOCATION_PLAYABILITY_TOKEN");"TVHTML5"===T("INNERTUBE_CLIENT_NAME")&&(this.h=Uu(this))&&(a=this.h.get("yt-location-playability-token"));a&&(this.locationPlayabilityToken=a,this.i=void 0)}
var Vu;function Wu(){Vu=E("yt.clientLocationService.instance");Vu||(Vu=new Tu,D("yt.clientLocationService.instance",Vu));return Vu}
m=Tu.prototype;
m.setLocationOnInnerTubeContext=function(a){a.client||(a.client={});if(this.i)a.client.locationInfo||(a.client.locationInfo={}),a.client.locationInfo.latitudeE7=Math.floor(1E7*this.i.coords.latitude),a.client.locationInfo.longitudeE7=Math.floor(1E7*this.i.coords.longitude),a.client.locationInfo.horizontalAccuracyMeters=Math.round(this.i.coords.accuracy),a.client.locationInfo.forceLocationPlayabilityTokenRefresh=!0;else if(this.l||this.locationPlayabilityToken)a.client.locationPlayabilityToken=this.l||
this.locationPlayabilityToken};
m.handleResponse=function(a){var b;a=null==(b=a.responseContext)?void 0:b.locationPlayabilityToken;void 0!==a&&(this.locationPlayabilityToken=a,this.i=void 0,"TVHTML5"===T("INNERTUBE_CLIENT_NAME")?(this.h=Uu(this))&&this.h.set("yt-location-playability-token",a,15552E3):jm("YT_CL",JSON.stringify({loctok:a}),15552E3,Su,!0))};
function Uu(a){return void 0===a.h?new kn("yt-client-location"):a.h}
m.clearLocationPlayabilityToken=function(a){"TVHTML5"===a?(this.h=Uu(this))&&this.h.remove("yt-location-playability-token"):lm("YT_CL");this.l=void 0;-1!==this.j&&(clearTimeout(this.j),this.j=-1)};
m.getCurrentPositionFromGeolocation=function(){var a=this;if(!(navigator&&navigator.geolocation&&navigator.geolocation.getCurrentPosition))return Promise.reject(Error("Geolocation unsupported"));var b=!1,c=1E4;"MWEB"===T("INNERTUBE_CLIENT_NAME")&&(b=!0,c=15E3);return new Promise(function(d,e){navigator.geolocation.getCurrentPosition(function(f){a.i=f;d(f)},function(f){e(f)},{enableHighAccuracy:b,
maximumAge:0,timeout:c})})};
m.createUnpluggedLocationInfo=function(a){var b={};a=a.coords;if(null==a?0:a.latitude)b.latitudeE7=Math.floor(1E7*a.latitude);if(null==a?0:a.longitude)b.longitudeE7=Math.floor(1E7*a.longitude);if(null==a?0:a.accuracy)b.locationRadiusMeters=Math.round(a.accuracy);return b};
m.createLocationInfo=function(a){var b={};a=a.coords;if(null==a?0:a.latitude)b.latitudeE7=Math.floor(1E7*a.latitude);if(null==a?0:a.longitude)b.longitudeE7=Math.floor(1E7*a.longitude);return b};function Xu(a){var b={"Content-Type":"application/json"};T("EOM_VISITOR_DATA")?b["X-Goog-EOM-Visitor-Id"]=T("EOM_VISITOR_DATA"):T("VISITOR_DATA")&&(b["X-Goog-Visitor-Id"]=T("VISITOR_DATA"));b["X-Youtube-Bootstrap-Logged-In"]=T("LOGGED_IN",!1);T("DEBUG_SETTINGS_METADATA")&&(b["X-Debug-Settings-Metadata"]=T("DEBUG_SETTINGS_METADATA"));"cors"!==a&&((a=T("INNERTUBE_CONTEXT_CLIENT_NAME"))&&(b["X-Youtube-Client-Name"]=a),(a=T("INNERTUBE_CONTEXT_CLIENT_VERSION"))&&(b["X-Youtube-Client-Version"]=a),(a=T("CHROME_CONNECTED_HEADER"))&&
(b["X-Youtube-Chrome-Connected"]=a),(a=T("DOMAIN_ADMIN_STATE"))&&(b["X-Youtube-Domain-Admin-State"]=a));return b}
;function Yu(){this.h={}}
Yu.prototype.contains=function(a){return Object.prototype.hasOwnProperty.call(this.h,a)};
Yu.prototype.get=function(a){if(this.contains(a))return this.h[a]};
Yu.prototype.set=function(a,b){this.h[a]=b};
Yu.prototype.remove=function(a){delete this.h[a]};function Zu(){this.mappings=new Yu}
Zu.prototype.getModuleId=function(a){return a.serviceId.getModuleId()};
Zu.prototype.get=function(a){a:{var b=this.mappings.get(a.toString());switch(b.type){case "mapping":a=b.value;break a;case "factory":b=b.value();this.mappings.set(a.toString(),{type:"mapping",value:b});a=b;break a;default:a=Xb(b)}}return a};
new Zu;function $u(a){return function(){return new a}}
;var av={},bv=(av.WEB_UNPLUGGED="^unplugged/",av.WEB_UNPLUGGED_ONBOARDING="^unplugged/",av.WEB_UNPLUGGED_OPS="^unplugged/",av.WEB_UNPLUGGED_PUBLIC="^unplugged/",av.WEB_CREATOR="^creator/",av.WEB_KIDS="^kids/",av.WEB_EXPERIMENTS="^experiments/",av.WEB_MUSIC="^music/",av.WEB_REMIX="^music/",av.WEB_MUSIC_EMBEDDED_PLAYER="^music/",av.WEB_MUSIC_EMBEDDED_PLAYER="^main_app/|^sfv/",av);
function cv(a){var b=void 0===b?"UNKNOWN_INTERFACE":b;if(1===a.length)return a[0];var c=bv[b];if(c){c=new RegExp(c);for(var d=x(a),e=d.next();!e.done;e=d.next())if(e=e.value,c.exec(e))return e}var f=[];Object.entries(bv).forEach(function(g){var h=x(g);g=h.next().value;h=h.next().value;b!==g&&f.push(h)});
c=new RegExp(f.join("|"));a.sort(function(g,h){return g.length-h.length});
d=x(a);for(e=d.next();!e.done;e=d.next())if(e=e.value,!c.exec(e))return e;return a[0]}
;function dv(){}
dv.prototype.v=function(a,b,c){b=void 0===b?{}:b;c=void 0===c?im:c;var d=a.clickTrackingParams,e=this.l,f=!1;f=void 0===f?!1:f;e=void 0===e?!1:e;var g=T("INNERTUBE_CONTEXT");if(g){g=Sb(g);U("web_no_tracking_params_in_shell_killswitch")||delete g.clickTracking;g.client||(g.client={});var h=g.client;"MWEB"===h.clientName&&"AUTOMOTIVE_FORM_FACTOR"!==h.clientFormFactor&&(h.clientFormFactor=T("IS_TABLET")?"LARGE_FORM_FACTOR":"SMALL_FORM_FACTOR");h.screenWidthPoints=window.innerWidth;h.screenHeightPoints=
window.innerHeight;h.screenPixelDensity=Math.round(window.devicePixelRatio||1);h.screenDensityFloat=window.devicePixelRatio||1;h.utcOffsetMinutes=-Math.floor((new Date).getTimezoneOffset());var k=void 0===k?!1:k;qm();var l="USER_INTERFACE_THEME_LIGHT";tm(165)?l="USER_INTERFACE_THEME_DARK":tm(174)?l="USER_INTERFACE_THEME_LIGHT":!U("kevlar_legacy_browsers")&&window.matchMedia&&window.matchMedia("(prefers-color-scheme)").matches&&window.matchMedia("(prefers-color-scheme: dark)").matches&&(l="USER_INTERFACE_THEME_DARK");
k=k?l:Pu()||l;h.userInterfaceTheme=k;if(!f){if(k=zm())h.connectionType=k;U("web_log_effective_connection_type")&&(k=Am())&&(g.client.effectiveConnectionType=k)}var n;if(U("web_log_memory_total_kbytes")&&(null==(n=B.navigator)?0:n.deviceMemory)){var p;n=null==(p=B.navigator)?void 0:p.deviceMemory;g.client.memoryTotalKbytes=""+1E6*n}U("web_gcf_hashes_innertube")&&(k=hp())&&(p=k.coldConfigData,n=k.coldHashData,k=k.hotHashData,g.client.configInfo=g.client.configInfo||{},p&&(g.client.configInfo.coldConfigData=
p),n&&(g.client.configInfo.coldHashData=n),k&&(g.client.configInfo.hotHashData=k));p=pl(B.location.href);!U("web_populate_internal_geo_killswitch")&&p.internalcountrycode&&(h.internalGeo=p.internalcountrycode);"MWEB"===h.clientName||"WEB"===h.clientName?(h.mainAppWebInfo={graftUrl:B.location.href},U("kevlar_woffle")&&dm.h&&(p=dm.h,h.mainAppWebInfo.pwaInstallabilityStatus=!p.h&&p.i?"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED":"PWA_INSTALLABILITY_STATUS_UNKNOWN"),h.mainAppWebInfo.webDisplayMode=em(),
h.mainAppWebInfo.isWebNativeShareAvailable=navigator&&void 0!==navigator.share):"TVHTML5"===h.clientName&&(!U("web_lr_app_quality_killswitch")&&(p=T("LIVING_ROOM_APP_QUALITY"))&&(h.tvAppInfo=Object.assign(h.tvAppInfo||{},{appQuality:p})),p=T("LIVING_ROOM_CERTIFICATION_SCOPE"))&&(h.tvAppInfo=Object.assign(h.tvAppInfo||{},{certificationScope:p}));if(!U("web_populate_time_zone_itc_killswitch")){b:{if("undefined"!==typeof Intl)try{var r=(new Intl.DateTimeFormat).resolvedOptions().timeZone;break b}catch(ea){}r=
void 0}r&&(h.timeZone=r)}(r=T("EXPERIMENTS_TOKEN",""))?h.experimentsToken=r:delete h.experimentsToken;r=Bl();Qu.h||(Qu.h=new Qu);h=Qu.h.h;p=[];n=0;for(var t in h)p[n++]=h[t];g.request=Object.assign({},g.request,{internalExperimentFlags:r,consistencyTokenJars:p});!U("web_prequest_context_killswitch")&&(t=T("INNERTUBE_CONTEXT_PREQUEST_CONTEXT"))&&(g.request.externalPrequestContext=t);r=qm();t=tm(58);r=r.get("gsml","");g.user=Object.assign({},g.user);t&&(g.user.enableSafetyMode=t);r&&(g.user.lockedSafetyMode=
!0);U("warm_op_csn_cleanup")?e&&(f=tt())&&(g.clientScreenNonce=f):!f&&(f=tt())&&(g.clientScreenNonce=f);d&&(g.clickTracking={clickTrackingParams:d});if(d=E("yt.mdx.remote.remoteClient_"))g.remoteClient=d;Wu().setLocationOnInnerTubeContext(g);try{var v=sl(),w=v.bid;delete v.bid;g.adSignalsInfo={params:[],bid:w};var C=x(Object.entries(v));for(var F=C.next();!F.done;F=C.next()){var K=x(F.value),N=K.next().value,S=K.next().value;v=N;w=S;d=void 0;null==(d=g.adSignalsInfo.params)||d.push({key:v,value:""+
w})}var da;if(U("add_ifa_to_tvh5_requests")&&"TVHTML5"===(null==(da=g.client)?void 0:da.clientName)){var ta=T("INNERTUBE_CONTEXT");ta.adSignalsInfo&&(g.adSignalsInfo.advertisingId=ta.adSignalsInfo.advertisingId,g.adSignalsInfo.advertisingIdSignalType="DEVICE_ID_TYPE_CONNECTED_TV_IFA",g.adSignalsInfo.limitAdTracking=ta.adSignalsInfo.limitAdTracking)}}catch(ea){at(ea)}C=g}else at(Error("Error: No InnerTubeContext shell provided in ytconfig.")),C={};C={context:C};if(F=this.i(a)){this.h(C,F,b);var P;
b="/youtubei/v1/"+cv(this.j());(F=null==(P=js(a.commandMetadata,Kk))?void 0:P.apiUrl)&&(b=F);P=b;(b=T("INNERTUBE_HOST_OVERRIDE"))&&(P=String(b)+String(pc(P)));b={};U("web_api_key_killswitch")&&(b.key=T("INNERTUBE_API_KEY"));U("json_condensed_response")&&(b.prettyPrint="false");P=ql(P,b||{},!1);a=Object.assign({},{command:a},void 0);a={input:P,ib:Et(P),Oa:C,config:a};a.config.Xb?a.config.Xb.identity=c:a.config.Xb={identity:c};return a}at(new V("Error: Failed to create Request from Command.",a))};
fa.Object.defineProperties(dv.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!1}}});
function ev(){}
y(ev,dv);function fv(){}
y(fv,ev);fv.prototype.v=function(){return{input:"/getDatasyncIdsEndpoint",ib:Et("/getDatasyncIdsEndpoint","GET"),Oa:{}}};
fv.prototype.j=function(){return[]};
fv.prototype.i=function(){};
fv.prototype.h=function(){};var gv={},hv=(gv.GET_DATASYNC_IDS=$u(fv),gv);function iv(a){var b;(b=E("ytcsi."+(a||"")+"data_"))||(b={tick:{},info:{}},D("ytcsi."+(a||"")+"data_",b));return b}
function jv(){var a=iv();a.info||(a.info={});return a.info}
function kv(a){a=iv(a);a.metadata||(a.metadata={});return a.metadata}
function lv(a){a=iv(a);a.tick||(a.tick={});return a.tick}
function mv(a){a=iv(a);if(a.gel){var b=a.gel;b.gelInfos||(b.gelInfos={});b.gelTicks||(b.gelTicks={})}else a.gel={gelTicks:{},gelInfos:{}};return a.gel}
function nv(a){a=mv(a);a.gelInfos||(a.gelInfos={});return a.gelInfos}
function ov(a){var b=iv(a).nonce;b||(b=jt(),iv(a).nonce=b);return b}
;function pv(){var a=E("ytcsi.debug");a||(a=[],D("ytcsi.debug",a),D("ytcsi.reference",{}));return a}
function qv(a){a=a||"";var b=E("ytcsi.reference");b||(pv(),b=E("ytcsi.reference"));if(b[a])return b[a];var c=pv(),d={timerName:a,info:{},tick:{},span:{},jspbInfo:[]};c.push(d);return b[a]=d}
;var X={},rv=(X.auto_search="LATENCY_ACTION_AUTO_SEARCH",X.ad_to_ad="LATENCY_ACTION_AD_TO_AD",X.ad_to_video="LATENCY_ACTION_AD_TO_VIDEO",X["analytics.explore"]="LATENCY_ACTION_CREATOR_ANALYTICS_EXPLORE",X.app_startup="LATENCY_ACTION_APP_STARTUP",X["artist.analytics"]="LATENCY_ACTION_CREATOR_ARTIST_ANALYTICS",X["artist.events"]="LATENCY_ACTION_CREATOR_ARTIST_CONCERTS",X["artist.presskit"]="LATENCY_ACTION_CREATOR_ARTIST_PROFILE",X["asset.claimed_videos"]="LATENCY_ACTION_CREATOR_CMS_ASSET_CLAIMED_VIDEOS",
X["asset.composition"]="LATENCY_ACTION_CREATOR_CMS_ASSET_COMPOSITION",X["asset.composition_ownership"]="LATENCY_ACTION_CREATOR_CMS_ASSET_COMPOSITION_OWNERSHIP",X["asset.composition_policy"]="LATENCY_ACTION_CREATOR_CMS_ASSET_COMPOSITION_POLICY",X["asset.embeds"]="LATENCY_ACTION_CREATOR_CMS_ASSET_EMBEDS",X["asset.history"]="LATENCY_ACTION_CREATOR_CMS_ASSET_HISTORY",X["asset.issues"]="LATENCY_ACTION_CREATOR_CMS_ASSET_ISSUES",X["asset.licenses"]="LATENCY_ACTION_CREATOR_CMS_ASSET_LICENSES",X["asset.metadata"]=
"LATENCY_ACTION_CREATOR_CMS_ASSET_METADATA",X["asset.ownership"]="LATENCY_ACTION_CREATOR_CMS_ASSET_OWNERSHIP",X["asset.policy"]="LATENCY_ACTION_CREATOR_CMS_ASSET_POLICY",X["asset.references"]="LATENCY_ACTION_CREATOR_CMS_ASSET_REFERENCES",X["asset.shares"]="LATENCY_ACTION_CREATOR_CMS_ASSET_SHARES",X["asset.sound_recordings"]="LATENCY_ACTION_CREATOR_CMS_ASSET_SOUND_RECORDINGS",X["asset_group.assets"]="LATENCY_ACTION_CREATOR_CMS_ASSET_GROUP_ASSETS",X["asset_group.campaigns"]="LATENCY_ACTION_CREATOR_CMS_ASSET_GROUP_CAMPAIGNS",
X["asset_group.claimed_videos"]="LATENCY_ACTION_CREATOR_CMS_ASSET_GROUP_CLAIMED_VIDEOS",X["asset_group.metadata"]="LATENCY_ACTION_CREATOR_CMS_ASSET_GROUP_METADATA",X["song.analytics"]="LATENCY_ACTION_CREATOR_SONG_ANALYTICS",X.browse="LATENCY_ACTION_BROWSE",X.cast_splash="LATENCY_ACTION_CAST_SPLASH",X.channels="LATENCY_ACTION_CHANNELS",X.creator_channel_dashboard="LATENCY_ACTION_CREATOR_CHANNEL_DASHBOARD",X["channel.analytics"]="LATENCY_ACTION_CREATOR_CHANNEL_ANALYTICS",X["channel.comments"]="LATENCY_ACTION_CREATOR_CHANNEL_COMMENTS",
X["channel.content"]="LATENCY_ACTION_CREATOR_POST_LIST",X["channel.content.promotions"]="LATENCY_ACTION_CREATOR_PROMOTION_LIST",X["channel.copyright"]="LATENCY_ACTION_CREATOR_CHANNEL_COPYRIGHT",X["channel.editing"]="LATENCY_ACTION_CREATOR_CHANNEL_EDITING",X["channel.monetization"]="LATENCY_ACTION_CREATOR_CHANNEL_MONETIZATION",X["channel.music"]="LATENCY_ACTION_CREATOR_CHANNEL_MUSIC",X["channel.music_storefront"]="LATENCY_ACTION_CREATOR_CHANNEL_MUSIC_STOREFRONT",X["channel.playlists"]="LATENCY_ACTION_CREATOR_CHANNEL_PLAYLISTS",
X["channel.translations"]="LATENCY_ACTION_CREATOR_CHANNEL_TRANSLATIONS",X["channel.videos"]="LATENCY_ACTION_CREATOR_CHANNEL_VIDEOS",X["channel.live_streaming"]="LATENCY_ACTION_CREATOR_LIVE_STREAMING",X.chips="LATENCY_ACTION_CHIPS",X.commerce_transaction="LATENCY_ACTION_COMMERCE_TRANSACTION",X["dialog.copyright_strikes"]="LATENCY_ACTION_CREATOR_DIALOG_COPYRIGHT_STRIKES",X["dialog.video_copyright"]="LATENCY_ACTION_CREATOR_DIALOG_VIDEO_COPYRIGHT",X["dialog.uploads"]="LATENCY_ACTION_CREATOR_DIALOG_UPLOADS",
X.direct_playback="LATENCY_ACTION_DIRECT_PLAYBACK",X.embed="LATENCY_ACTION_EMBED",X.entity_key_serialization_perf="LATENCY_ACTION_ENTITY_KEY_SERIALIZATION_PERF",X.entity_key_deserialization_perf="LATENCY_ACTION_ENTITY_KEY_DESERIALIZATION_PERF",X.explore="LATENCY_ACTION_EXPLORE",X.favorites="LATENCY_ACTION_FAVORITES",X.home="LATENCY_ACTION_HOME",X.inboarding="LATENCY_ACTION_INBOARDING",X.library="LATENCY_ACTION_LIBRARY",X.live="LATENCY_ACTION_LIVE",X.live_pagination="LATENCY_ACTION_LIVE_PAGINATION",
X.mini_app="LATENCY_ACTION_MINI_APP_PLAY",X.notification_settings="LATENCY_ACTION_KIDS_NOTIFICATION_SETTINGS",X.onboarding="LATENCY_ACTION_ONBOARDING",X.owner="LATENCY_ACTION_CREATOR_CMS_DASHBOARD",X["owner.allowlist"]="LATENCY_ACTION_CREATOR_CMS_ALLOWLIST",X["owner.analytics"]="LATENCY_ACTION_CREATOR_CMS_ANALYTICS",X["owner.art_tracks"]="LATENCY_ACTION_CREATOR_CMS_ART_TRACKS",X["owner.assets"]="LATENCY_ACTION_CREATOR_CMS_ASSETS",X["owner.asset_groups"]="LATENCY_ACTION_CREATOR_CMS_ASSET_GROUPS",X["owner.bulk"]=
"LATENCY_ACTION_CREATOR_CMS_BULK_HISTORY",X["owner.campaigns"]="LATENCY_ACTION_CREATOR_CMS_CAMPAIGNS",X["owner.channel_invites"]="LATENCY_ACTION_CREATOR_CMS_CHANNEL_INVITES",X["owner.channels"]="LATENCY_ACTION_CREATOR_CMS_CHANNELS",X["owner.claimed_videos"]="LATENCY_ACTION_CREATOR_CMS_CLAIMED_VIDEOS",X["owner.claims"]="LATENCY_ACTION_CREATOR_CMS_MANUAL_CLAIMING",X["owner.claims.manual"]="LATENCY_ACTION_CREATOR_CMS_MANUAL_CLAIMING",X["owner.delivery"]="LATENCY_ACTION_CREATOR_CMS_CONTENT_DELIVERY",
X["owner.delivery_templates"]="LATENCY_ACTION_CREATOR_CMS_DELIVERY_TEMPLATES",X["owner.issues"]="LATENCY_ACTION_CREATOR_CMS_ISSUES",X["owner.licenses"]="LATENCY_ACTION_CREATOR_CMS_LICENSES",X["owner.pitch_music"]="LATENCY_ACTION_CREATOR_CMS_PITCH_MUSIC",X["owner.policies"]="LATENCY_ACTION_CREATOR_CMS_POLICIES",X["owner.releases"]="LATENCY_ACTION_CREATOR_CMS_RELEASES",X["owner.reports"]="LATENCY_ACTION_CREATOR_CMS_REPORTS",X["owner.videos"]="LATENCY_ACTION_CREATOR_CMS_VIDEOS",X.parent_profile_settings=
"LATENCY_ACTION_KIDS_PARENT_PROFILE_SETTINGS",X.parent_tools_collection="LATENCY_ACTION_PARENT_TOOLS_COLLECTION",X.parent_tools_dashboard="LATENCY_ACTION_PARENT_TOOLS_DASHBOARD",X.player_att="LATENCY_ACTION_PLAYER_ATTESTATION",X["playlist.videos"]="LATENCY_ACTION_CREATOR_PLAYLIST_VIDEO_LIST",X["post.comments"]="LATENCY_ACTION_CREATOR_POST_COMMENTS",X["post.edit"]="LATENCY_ACTION_CREATOR_POST_EDIT",X.prebuffer="LATENCY_ACTION_PREBUFFER",X.prefetch="LATENCY_ACTION_PREFETCH",X.profile_settings="LATENCY_ACTION_KIDS_PROFILE_SETTINGS",
X.profile_switcher="LATENCY_ACTION_LOGIN",X.reel_watch="LATENCY_ACTION_REEL_WATCH",X.results="LATENCY_ACTION_RESULTS",X["promotion.edit"]="LATENCY_ACTION_CREATOR_PROMOTION_EDIT",X.red="LATENCY_ACTION_PREMIUM_PAGE_GET_BROWSE",X.premium="LATENCY_ACTION_PREMIUM_PAGE_GET_BROWSE",X.search_overview_answer="LATENCY_ACTION_SEARCH_OVERVIEW_ANSWER",X.search_ui="LATENCY_ACTION_SEARCH_UI",X.search_suggest="LATENCY_ACTION_SUGGEST",X.search_zero_state="LATENCY_ACTION_SEARCH_ZERO_STATE",X.secret_code="LATENCY_ACTION_KIDS_SECRET_CODE",
X.seek="LATENCY_ACTION_PLAYER_SEEK",X.settings="LATENCY_ACTION_SETTINGS",X.store="LATENCY_ACTION_STORE",X.supervision_dashboard="LATENCY_ACTION_KIDS_SUPERVISION_DASHBOARD",X.tenx="LATENCY_ACTION_TENX",X.video_to_ad="LATENCY_ACTION_VIDEO_TO_AD",X.watch="LATENCY_ACTION_WATCH",X.watch_it_again="LATENCY_ACTION_KIDS_WATCH_IT_AGAIN",X["watch,watch7"]="LATENCY_ACTION_WATCH",X["watch,watch7_html5"]="LATENCY_ACTION_WATCH",X["watch,watch7ad"]="LATENCY_ACTION_WATCH",X["watch,watch7ad_html5"]="LATENCY_ACTION_WATCH",
X.wn_comments="LATENCY_ACTION_LOAD_COMMENTS",X.ww_rqs="LATENCY_ACTION_WHO_IS_WATCHING",X["video.analytics"]="LATENCY_ACTION_CREATOR_VIDEO_ANALYTICS",X["video.claims"]="LATENCY_ACTION_CREATOR_VIDEO_CLAIMS",X["video.comments"]="LATENCY_ACTION_CREATOR_VIDEO_COMMENTS",X["video.copyright"]="LATENCY_ACTION_CREATOR_VIDEO_COPYRIGHT",X["video.edit"]="LATENCY_ACTION_CREATOR_VIDEO_EDIT",X["video.editor"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR",X["video.editor_async"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR_ASYNC",
X["video.live_settings"]="LATENCY_ACTION_CREATOR_VIDEO_LIVE_SETTINGS",X["video.live_streaming"]="LATENCY_ACTION_CREATOR_VIDEO_LIVE_STREAMING",X["video.monetization"]="LATENCY_ACTION_CREATOR_VIDEO_MONETIZATION",X["video.policy"]="LATENCY_ACTION_CREATOR_VIDEO_POLICY",X["video.rights_management"]="LATENCY_ACTION_CREATOR_VIDEO_RIGHTS_MANAGEMENT",X["video.translations"]="LATENCY_ACTION_CREATOR_VIDEO_TRANSLATIONS",X.voice_assistant="LATENCY_ACTION_VOICE_ASSISTANT",X.cast_load_by_entity_to_watch="LATENCY_ACTION_CAST_LOAD_BY_ENTITY_TO_WATCH",
X.networkless_performance="LATENCY_ACTION_NETWORKLESS_PERFORMANCE",X.gel_compression="LATENCY_ACTION_GEL_COMPRESSION",X.gel_jspb_serialize="LATENCY_ACTION_GEL_JSPB_SERIALIZE",X);function sv(a,b){op.call(this,1,arguments);this.timer=b}
y(sv,op);var tv=new pp("aft-recorded",sv);var uv=B.ytLoggingLatencyUsageStats_||{};D("ytLoggingLatencyUsageStats_",uv);function vv(){this.h=0}
function wv(){vv.h||(vv.h=new vv);return vv.h}
vv.prototype.tick=function(a,b,c,d){xv(this,"tick_"+a+"_"+b)||tn("latencyActionTicked",{tickName:a,clientActionNonce:b},{timestamp:c,cttAuthInfo:d})};
vv.prototype.info=function(a,b,c){var d=Object.keys(a).join("");xv(this,"info_"+d+"_"+b)||(a=Object.assign({},a),a.clientActionNonce=b,tn("latencyActionInfo",a,{cttAuthInfo:c}))};
vv.prototype.jspbInfo=function(){};
vv.prototype.span=function(a,b,c){var d=Object.keys(a).join("");xv(this,"span_"+d+"_"+b)||(a.clientActionNonce=b,tn("latencyActionSpan",a,{cttAuthInfo:c}))};
function xv(a,b){uv[b]=uv[b]||{count:0};var c=uv[b];c.count++;c.time=W();a.h||(a.h=Em(function(){var d=W(),e;for(e in uv)uv[e]&&6E4<d-uv[e].time&&delete uv[e];a&&(a.h=0)},5E3));
return 5<c.count?(6===c.count&&1>1E5*Math.random()&&(c=new V("CSI data exceeded logging limit with key",b.split("_")),0<=b.indexOf("plev")||bt(c)),!0):!1}
;var yv=window;function zv(){this.timing={};this.clearResourceTimings=function(){};
this.webkitClearResourceTimings=function(){};
this.mozClearResourceTimings=function(){};
this.msClearResourceTimings=function(){};
this.oClearResourceTimings=function(){}}
function Av(){var a;if(U("csi_use_performance_navigation_timing")||U("csi_use_performance_navigation_timing_tvhtml5")){var b,c,d,e=null==Y?void 0:null==(a=Y.getEntriesByType)?void 0:null==(b=a.call(Y,"navigation"))?void 0:null==(c=b[0])?void 0:null==(d=c.toJSON)?void 0:d.call(c);e?(e.requestStart=Bv(e.requestStart),e.responseEnd=Bv(e.responseEnd),e.redirectStart=Bv(e.redirectStart),e.redirectEnd=Bv(e.redirectEnd),e.domainLookupEnd=Bv(e.domainLookupEnd),e.connectStart=Bv(e.connectStart),e.connectEnd=
Bv(e.connectEnd),e.responseStart=Bv(e.responseStart),e.secureConnectionStart=Bv(e.secureConnectionStart),e.domainLookupStart=Bv(e.domainLookupStart),e.isPerformanceNavigationTiming=!0,a=e):a=Y.timing}else a=U("csi_performance_timing_to_object")?JSON.parse(JSON.stringify(Y.timing)):Y.timing;return a}
function Bv(a){return Math.round(Cv()+a)}
function Cv(){return(U("csi_use_time_origin")||U("csi_use_time_origin_tvhtml5"))&&Y.timeOrigin?Math.floor(Y.timeOrigin):Y.timing.navigationStart}
var Y=yv.performance||yv.mozPerformance||yv.msPerformance||yv.webkitPerformance||new zv;var Dv=!1,Ev=!1,Fv={'script[name="scheduler/scheduler"]':"sj",'script[name="player/base"]':"pj",'link[rel="preload"][name="player/embed"]':"pej",'link[rel="stylesheet"][name="www-player"]':"pc",'link[rel="stylesheet"][name="player/www-player"]':"pc",'script[name="desktop_polymer/desktop_polymer"]':"dpj",'link[rel="import"][name="desktop_polymer"]':"dph",'script[name="mobile-c3"]':"mcj",'link[rel="stylesheet"][name="mobile-c3"]':"mcc",'script[name="player-plasma-ias-phone/base"]':"mcppj",'script[name="player-plasma-ias-tablet/base"]':"mcptj",
'link[rel="stylesheet"][name="mobile-polymer-player-ias"]':"mcpc",'link[rel="stylesheet"][name="mobile-polymer-player-svg-ias"]':"mcpsc",'script[name="mobile_blazer_core_mod"]':"mbcj",'link[rel="stylesheet"][name="mobile_blazer_css"]':"mbc",'script[name="mobile_blazer_logged_in_users_mod"]':"mbliuj",'script[name="mobile_blazer_logged_out_users_mod"]':"mblouj",'script[name="mobile_blazer_noncore_mod"]':"mbnj","#player_css":"mbpc",'script[name="mobile_blazer_desktopplayer_mod"]':"mbpj",'link[rel="stylesheet"][name="mobile_blazer_tablet_css"]':"mbtc",
'script[name="mobile_blazer_watch_mod"]':"mbwj"};Xa(Y.clearResourceTimings||Y.webkitClearResourceTimings||Y.mozClearResourceTimings||Y.msClearResourceTimings||Y.oClearResourceTimings||Bd,Y);function Gv(a,b){if(!U("web_csi_action_sampling_enabled")||!iv(b).actionDisabled){var c=qv(b||"");lu(c.info,a);a.loadType&&(c=a.loadType,kv(b).loadType=c);lu(nv(b),a);c=ov(b);b=iv(b).cttAuthInfo;wv().info(a,c,b)}}
function Hv(){var a,b,c,d;return(null!=(d=null==Mr().resolve(new Gr(dp))?void 0:null==(a=ep())?void 0:null==(b=a.loggingHotConfig)?void 0:null==(c=b.csiConfig)?void 0:c.debugTicks)?d:[]).map(function(e){return Object.values(e)[0]})}
function Z(a,b,c){if(!U("web_csi_action_sampling_enabled")||!iv(c).actionDisabled){var d=ov(c),e;if(e=U("web_csi_debug_sample_enabled")&&d){(null==Mr().resolve(new Gr(dp))?0:ep())&&!Ev&&(Ev=!0,Z("gcfl",W(),c));var f,g,h;e=(null==Mr().resolve(new Gr(dp))?void 0:null==(f=ep())?void 0:null==(g=f.loggingHotConfig)?void 0:null==(h=g.csiConfig)?void 0:h.debugSampleWeight)||0;if(f=0!==e)b:{f=Hv();if(0<f.length)for(g=0;g<f.length;g++)if(a===f[g]){f=!0;break b}f=!1}if(f){for(g=f=0;g<d.length;g++)f=31*f+d.charCodeAt(g),
g<d.length-1&&(f%=Math.pow(2,47));e=0!==f%1E5%e;iv(c).debugTicksExcludedLogged||(f={},f.debugTicksExcluded=e,Gv(f,c));iv(c).debugTicksExcludedLogged=!0}else e=!1}if(!e){if("_"!==a[0]&&(e=a,f=b,Y.mark))if(e.startsWith("mark_")||(e="mark_"+e),c&&(e+=" ("+c+")"),void 0===f||U("web_csi_disable_alt_time_performance_mark"))Y.mark(e);else{f-=Y.timeOrigin||Y.timing.navigationStart;try{Y.mark(e,{startTime:f})}catch(k){}}e=qv(c||"");e.tick[a]=b||W();if(e.callback&&e.callback[a])for(e=x(e.callback[a]),f=e.next();!f.done;f=
e.next())f=f.value,f();e=mv(c);e.gelTicks&&(e.gelTicks[a]=!0);f=lv(c);e=b||W();U("log_repeated_ytcsi_ticks")?a in f||(f[a]=e):f[a]=e;f=iv(c).cttAuthInfo;"_start"===a?(a=wv(),xv(a,"baseline_"+d)||tn("latencyActionBaselined",{clientActionNonce:d},{timestamp:b,cttAuthInfo:f})):wv().tick(a,d,b,f);Iv(c);return e}}}
function Jv(){var a=document;if("visibilityState"in a)a=a.visibilityState;else{var b=cr+"VisibilityState";a=b in a?a[b]:void 0}switch(a){case "hidden":return 0;case "visible":return 1;case "prerender":return 2;case "unloaded":return 3;default:return-1}}
function Kv(){function a(f,g,h){g=g.match("_rid")?g.split("_rid")[0]:g;"number"===typeof h&&(h=JSON.stringify(h));f.requestIds?f.requestIds.push({endpoint:g,id:h}):f.requestIds=[{endpoint:g,id:h}]}
for(var b={},c=x(Object.entries(T("TIMING_INFO",{}))),d=c.next();!d.done;d=c.next()){var e=x(d.value);d=e.next().value;e=e.next().value;switch(d){case "GetBrowse_rid":a(b,d,e);break;case "GetGuide_rid":a(b,d,e);break;case "GetHome_rid":a(b,d,e);break;case "GetPlayer_rid":a(b,d,e);break;case "GetSearch_rid":a(b,d,e);break;case "GetSettings_rid":a(b,d,e);break;case "GetTrending_rid":a(b,d,e);break;case "GetWatchNext_rid":a(b,d,e);break;case "yt_red":b.isRedSubscriber=!!e;break;case "yt_ad":b.isMonetized=
!!e}}return b}
function Lv(a,b){a=document.querySelector(a);if(!a)return!1;var c="",d=a.nodeName;"SCRIPT"===d?(c=a.src,c||(c=a.getAttribute("data-timing-href"))&&(c=window.location.protocol+c)):"LINK"===d&&(c=a.href);$b(window)&&a.setAttribute("nonce",$b(window));return c?(a=Y.getEntriesByName(c))&&a[0]&&(a=a[0],c=Cv(),Z("rsf_"+b,c+Math.round(a.fetchStart)),Z("rse_"+b,c+Math.round(a.responseEnd)),void 0!==a.transferSize&&0===a.transferSize)?!0:!1:!1}
function Mv(){var a=window.location.protocol,b=Y.getEntriesByType("resource");b=Eb(b,function(c){return 0===c.name.indexOf(a+"//fonts.gstatic.com/s/")});
(b=Gb(b,function(c,d){return d.duration>c.duration?d:c},{duration:0}))&&0<b.startTime&&0<b.responseEnd&&(Z("wffs",Bv(b.startTime)),Z("wffe",Bv(b.responseEnd)))}
function Nv(a){var b=Ov("aft",a);if(b)return b;b=T((a||"")+"TIMING_AFT_KEYS",["ol"]);for(var c=b.length,d=0;d<c;d++){var e=Ov(b[d],a);if(e)return e}return NaN}
function Ov(a,b){if(a=lv(b)[a])return"number"===typeof a?a:a[a.length-1]}
function Iv(a){var b=Ov("_start",a),c=Nv(a),d=U("enable_cow_info_csi")||!Dv;b&&c&&d&&(up(tv,new sv(Math.round(c-b),a)),Dv=!0)}
function Pv(){if(Y.getEntriesByType){var a=Y.getEntriesByType("paint");if(a=Hb(a,function(b){return"first-paint"===b.name}))return Bv(a.startTime)}a=Y.timing;
return a.ye?Math.max(0,a.ye):0}
;function Qv(a,b){fl(function(){qv("").info.actionType=a;b&&bl("TIMING_AFT_KEYS",b);bl("TIMING_ACTION",a);var c=Kv();0<Object.keys(c).length&&Gv(c);c={isNavigation:!0,actionType:rv[T("TIMING_ACTION")]||"LATENCY_ACTION_UNKNOWN"};var d=T("PREVIOUS_ACTION");d&&(c.previousAction=rv[d]||"LATENCY_ACTION_UNKNOWN");if(d=T("CLIENT_PROTOCOL"))c.httpProtocol=d;if(d=T("CLIENT_TRANSPORT"))c.transportProtocol=d;(d=tt())&&"UNDEFINED_CSN"!==d&&(c.clientScreenNonce=d);d=Jv();if(1===d||-1===d)c.isVisible=!0;kv();jv();
c.loadType="cold";d=jv();var e=Av(),f=Cv(),g=T("CSI_START_TIMESTAMP_MILLIS",0);0<g&&!U("embeds_web_enable_csi_start_override_killswitch")&&(f=g);f&&(Z("srt",e.responseStart),1!==d.prerender&&Z("_start",f,void 0));d=Pv();0<d&&Z("fpt",d);d=Av();d.isPerformanceNavigationTiming&&Gv({performanceNavigationTiming:!0},void 0);Z("nreqs",d.requestStart,void 0);Z("nress",d.responseStart,void 0);Z("nrese",d.responseEnd,void 0);0<d.redirectEnd-d.redirectStart&&(Z("nrs",d.redirectStart,void 0),Z("nre",d.redirectEnd,
void 0));0<d.domainLookupEnd-d.domainLookupStart&&(Z("ndnss",d.domainLookupStart,void 0),Z("ndnse",d.domainLookupEnd,void 0));0<d.connectEnd-d.connectStart&&(Z("ntcps",d.connectStart,void 0),Z("ntcpe",d.connectEnd,void 0));d.secureConnectionStart>=Cv()&&0<d.connectEnd-d.secureConnectionStart&&(Z("nstcps",d.secureConnectionStart,void 0),Z("ntcpe",d.connectEnd,void 0));Y&&"getEntriesByType"in Y&&Mv();d=[];if(document.querySelector&&Y&&Y.getEntriesByName)for(var h in Fv)Fv.hasOwnProperty(h)&&(e=Fv[h],
Lv(h,e)&&d.push(e));if(0<d.length)for(c.resourceInfo=[],h=x(d),d=h.next();!d.done;d=h.next())c.resourceInfo.push({resourceCache:d.value});Gv(c);c=mv();c.preLoggedGelInfos||(c.preLoggedGelInfos=[]);h=c.preLoggedGelInfos;c=nv();d=void 0;for(e=0;e<h.length;e++)if(f=h[e],f.loadType){d=f.loadType;break}if("cold"===kv().loadType&&("cold"===c.loadType||"cold"===d)){d=lv();e=mv();e=e.gelTicks?e.gelTicks:e.gelTicks={};for(var k in d)if(!(k in e))if("number"===typeof d[k])Z(k,Ov(k));else if(U("log_repeated_ytcsi_ticks"))for(f=
x(d[k]),g=f.next();!g.done;g=f.next())g=g.value,Z(k.slice(1),g);k={};d=!1;h=x(h);for(e=h.next();!e.done;e=h.next())d=e.value,lu(c,d),lu(k,d),d=!0;d&&Gv(k)}D("ytglobal.timingready_",!0);k=T("TIMING_ACTION");E("ytglobal.timingready_")&&k&&Rv()&&Nv()&&Iv()})()}
function Rv(){return fl(function(){return Sv()})()}
function Tv(a,b,c){fl(Gv)(a,b,void 0===c?!1:c)}
function Uv(a,b,c){return fl(Z)(a,b,c)}
function Sv(){return fl(function(){return"_start"in lv()})()}
function Vv(){fl(function(){var a=ov();requestAnimationFrame(function(){setTimeout(function(){a===ov()&&Uv("ol",void 0,void 0)},0)})})()}
var Wv=window;Wv.ytcsi&&(Wv.ytcsi.infoGel=Tv,Wv.ytcsi.tick=Uv);var Xv="tokens consistency mss client_location entities adblock_detection response_received_commands store PLAYER_PRELOAD".split(" "),Yv=["type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.BrowseResponse","type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.PlayerResponse"];function Zv(a,b,c,d){this.v=a;this.fa=b;this.l=c;this.j=d;this.i=void 0;this.h=new Map;a.Sb||(a.Sb={});a.Sb=Object.assign({},hv,a.Sb)}
function $v(a,b,c,d){if(void 0!==Zv.h){if(d=Zv.h,a=[a!==d.v,b!==d.fa,c!==d.l,!1,!1,!1,void 0!==d.i],a.some(function(e){return e}))throw new V("InnerTubeTransportService is already initialized",a);
}else Zv.h=new Zv(a,b,c,d)}
function aw(a){var b={signalServiceEndpoint:{signal:"GET_DATASYNC_IDS"}};var c=void 0===c?im:c;var d=bw(a,b);return d?new Ud(function(e,f){var g,h,k,l,n;return z(function(p){switch(p.h){case 1:return p.yield(d,2);case 2:g=p.i;h=g.v(b,void 0,c);if(!h){f(new V("Error: Failed to build request for command.",b));p.B(0);break}Lu(h.input);l="cors"===(null==(k=h.ib)?void 0:k.mode)?"cors":void 0;if(a.l.df){var r=h.config,t;r=null==r?void 0:null==(t=r.Xb)?void 0:t.sessionIndex;t=hm(0,{sessionIndex:r});n=Object.assign({},
Xu(l),t);p.B(4);break}return p.yield(cw(h.config,l),5);case 5:n=p.i;case 4:e(dw(a,h,n)),p.h=0}})}):Zd(new V("Error: No request builder found for command.",b))}
function ew(a,b,c){var d;if(b&&!(null==b?0:null==(d=b.sequenceMetaData)?0:d.skipProcessing)&&a.j){d=x(Xv);for(var e=d.next();!e.done;e=d.next())e=e.value,a.j[e]&&a.j[e].handleResponse(b,c)}}
function dw(a,b,c){var d=void 0===d?function(){}:d;
var e,f,g,h,k,l,n,p,r,t,v,w,C,F,K,N,S,da,ta,P,ea,na,La,Ka,Mg,Ng,rr,sr,tr;return z(function(ha){switch(ha.h){case 1:ha.B(2);break;case 3:if((e=ha.i)&&!e.isExpired())return ha.return(Promise.resolve(e.h()));case 2:if(!(null==(f=b)?0:null==(g=f.Oa)?0:g.context)){ha.B(4);break}h=b.Oa.context;ha.B(5);break;case 5:k=x([]),l=k.next();case 7:if(l.done){ha.B(4);break}n=l.value;return ha.yield(n.Sg(h),8);case 8:l=k.next();ha.B(7);break;case 4:if(null==(p=a.i)||!p.Xg(b.input,b.Oa)){ha.B(11);break}return ha.yield(a.i.Og(b.input,
b.Oa),12);case 12:return r=ha.i,U("kevlar_process_local_innertube_responses_killswitch")||ew(a,r,b),ha.return(r);case 11:return(w=null==(v=b.config)?void 0:v.Vg)&&a.h.has(w)?t=a.h.get(w):(C=JSON.stringify(b.Oa),N=null!=(K=null==(F=b.ib)?void 0:F.headers)?K:{},b.ib=Object.assign({},b.ib,{headers:Object.assign({},N,c)}),S=Object.assign({},b.ib),"POST"===b.ib.method&&(S=Object.assign({},S,{body:C})),(null==(da=b.config)?0:da.Ie)&&Uv(b.config.Ie),ta=function(){return a.fa.fetch(b.input,S,b.config)},t=
ta(),w&&a.h.set(w,t)),ha.yield(t,13);
case 13:if((P=ha.i)&&"error"in P&&(null==(ea=P)?0:null==(na=ea.error)?0:na.details))for(La=P.error.details,Ka=x(La),Mg=Ka.next();!Mg.done;Mg=Ka.next())Ng=Mg.value,(rr=Ng["@type"])&&-1<Yv.indexOf(rr)&&(delete Ng["@type"],P=Ng);w&&a.h.has(w)&&a.h.delete(w);(null==(sr=b.config)?0:sr.Je)&&Uv(b.config.Je);if(P||null==(tr=a.i)||!tr.Gg(b.input,b.Oa)){ha.B(14);break}return ha.yield(a.i.Ng(b.input,b.Oa),15);case 15:P=ha.i;case 14:return ew(a,P,b),d(),ha.return(P||void 0)}})}
function bw(a,b){a:{a=a.v;var c,d=null==(c=js(b,Lk))?void 0:c.signal;if(d&&a.Sb&&(c=a.Sb[d])){var e=c();break a}var f;if((c=null==(f=js(b,Jk))?void 0:f.request)&&a.Sd&&(f=a.Sd[c])){e=f();break a}for(e in b)if(a.Xc[e]&&(b=a.Xc[e])){e=b();break a}e=void 0}if(void 0!==e)return Promise.resolve(e)}
function cw(a,b){var c,d,e,f;return z(function(g){if(1==g.h){e=null==(c=a)?void 0:null==(d=c.Xb)?void 0:d.sessionIndex;var h=g.yield;var k=hm(0,{sessionIndex:e});if(!(k instanceof Ud)){var l=new Ud(Bd);Vd(l,2,k);k=l}return h.call(g,k,2)}f=g.i;return g.return(Promise.resolve(Object.assign({},Xu(b),f)))})}
;var fw=new Fr("INNERTUBE_TRANSPORT_TOKEN");function gw(){}
y(gw,ev);gw.prototype.j=function(){return Yt};
gw.prototype.i=function(a){return js(a,Tk)||void 0};
gw.prototype.h=function(a,b,c){c=void 0===c?{}:c;b.channelIds&&(a.channelIds=b.channelIds);b.siloName&&(a.siloName=b.siloName);b.params&&(a.params=b.params);c.botguardResponse&&(a.botguardResponse=c.botguardResponse);c.feature&&(a.clientFeature=c.feature)};
fa.Object.defineProperties(gw.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!0}}});function hw(){}
y(hw,ev);hw.prototype.j=function(){return Zt};
hw.prototype.i=function(a){return js(a,Sk)||void 0};
hw.prototype.h=function(a,b){b.channelIds&&(a.channelIds=b.channelIds);b.siloName&&(a.siloName=b.siloName);b.params&&(a.params=b.params)};
fa.Object.defineProperties(hw.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!0}}});function iw(){}
y(iw,ev);iw.prototype.j=function(){return Vt};
iw.prototype.i=function(a){return js(a,Nk)||void 0};
iw.prototype.h=function(a,b,c){a.feedbackTokens=[];b.feedbackToken&&a.feedbackTokens.push(b.feedbackToken);if(b=b.cpn||c.cpn)a.feedbackContext={cpn:b};a.isFeedbackTokenUnencrypted=!!c.is_feedback_token_unencrypted;a.shouldMerge=!1;c.extra_feedback_tokens&&(a.shouldMerge=!0,a.feedbackTokens=a.feedbackTokens.concat(c.extra_feedback_tokens))};
fa.Object.defineProperties(iw.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!0}}});function jw(){}
y(jw,ev);jw.prototype.j=function(){return Wt};
jw.prototype.i=function(a){return js(a,Rk)||void 0};
jw.prototype.h=function(a,b){b.params&&(a.params=b.params);b.secondaryParams&&(a.secondaryParams=b.secondaryParams)};function kw(){}
y(kw,ev);kw.prototype.j=function(){return Xt};
kw.prototype.i=function(a){return js(a,Qk)||void 0};
kw.prototype.h=function(a,b){b.actions&&(a.actions=b.actions);b.params&&(a.params=b.params);b.playlistId&&(a.playlistId=b.playlistId)};function lw(){}
y(lw,ev);lw.prototype.j=function(){return Ut};
lw.prototype.i=function(a){return js(a,Pk)};
lw.prototype.h=function(a,b,c){c=void 0===c?{}:c;b.serializedShareEntity&&(a.serializedSharedEntity=b.serializedShareEntity);c.includeListId&&(a.includeListId=!0)};function mw(a,b){var c=A.apply(2,arguments);a=void 0===a?0:a;V.call(this,b,c);this.errorType=a;Object.setPrototypeOf(this,this.constructor.prototype)}
y(mw,V);var nw=new Fr("NETWORK_SLI_TOKEN");function ow(a){this.h=a}
ow.prototype.fetch=function(a,b,c){var d=this,e;return z(function(f){e=pw(d,a,b);return f.return(fetch(e).then(function(g){return d.handleResponse(g,c)}).catch(function(g){bt(g);
if((null==c?0:c.Yd)&&g instanceof mw&&1===g.errorType)return Promise.reject(g)}))})};
function pw(a,b,c){if(a.h){var d=mc(nc(5,xc(b,"key")))||"/UNKNOWN_PATH";a.h.start(d)}a=c;U("wug_networking_gzip_request")&&(a=Wp(c));return new window.Request(b,a)}
ow.prototype.handleResponse=function(a,b){var c=a.text().then(function(d){if((null==b?0:b.re)&&a.ok)return Qg(b.re,d);d=d.replace(")]}'","");if((null==b?0:b.Yd)&&d)try{var e=JSON.parse(d)}catch(g){throw new mw(1,"JSON parsing failed after fetch");}var f;return null!=(f=e)?f:JSON.parse(d)});
a.redirected||a.ok?this.h&&this.h.success():(this.h&&this.h.Jg(),c=c.then(function(d){bt(new V("Error: API fetch failed",a.status,a.url,d));return Object.assign({},d,{errorMetadata:{status:a.status}})}));
return c};
ow[Er]=[new Gr(nw)];var qw=new Fr("NETWORK_MANAGER_TOKEN");var rw;function sw(){var a,b,c;return z(function(d){if(1==d.h)return a=Mr().resolve(fw),a?d.yield(aw(a),2):(bt(Error("InnertubeTransportService unavailable in fetchDatasyncIds")),d.return(void 0));if(b=d.i){if(b.errorMetadata)return bt(Error("Datasync IDs fetch responded with "+b.errorMetadata.status+": "+b.error)),d.return(void 0);c=b.Hg;return d.return(c)}bt(Error("Network request to get Datasync IDs failed."));return d.return(void 0)})}
;function tw(){var a;return null==(a=T("WEB_PLAYER_CONTEXT_CONFIGS"))?void 0:a.WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER}
;var uw=B.caches,vw;function ww(a){var b=a.indexOf(":");return-1===b?{od:a}:{od:a.substring(0,b),datasyncId:a.substring(b+1)}}
function xw(){return z(function(a){if(void 0!==vw)return a.return(vw);vw=new Promise(function(b){var c;return z(function(d){switch(d.h){case 1:return Aa(d,2),d.yield(uw.open("test-only"),4);case 4:return d.yield(uw.delete("test-only"),5);case 5:d.h=3;d.l=0;break;case 2:if(c=Ba(d),c instanceof Error&&"SecurityError"===c.name)return b(!1),d.return();case 3:b("caches"in window),d.h=0}})});
return a.return(vw)})}
function yw(a){var b,c,d,e,f,g,h;z(function(k){if(1==k.h)return k.yield(xw(),2);if(3!=k.h){if(!k.i)return k.return(!1);b=[];return k.yield(uw.keys(),3)}c=k.i;d=x(c);for(e=d.next();!e.done;e=d.next())f=e.value,g=ww(f),h=g.datasyncId,!h||a.includes(h)||b.push(uw.delete(f));return k.return(Promise.all(b).then(function(l){return l.some(function(n){return n})}))})}
function zw(){var a,b,c,d,e,f,g;return z(function(h){if(1==h.h)return h.yield(xw(),2);if(3!=h.h){if(!h.i)return h.return(!1);a=Cm("cache contains other");return h.yield(uw.keys(),3)}b=h.i;c=x(b);for(d=c.next();!d.done;d=c.next())if(e=d.value,f=ww(e),(g=f.datasyncId)&&g!==a)return h.return(!0);return h.return(!1)})}
;function Aw(){try{return!!self.sessionStorage}catch(a){return!1}}
;function Bw(a){a=a.match(/(.*)::.*::.*/);if(null!==a)return a[1]}
function Cw(a){if(Aw()){var b=Object.keys(window.sessionStorage);b=x(b);for(var c=b.next();!c.done;c=b.next()){c=c.value;var d=Bw(c);void 0===d||a.includes(d)||self.sessionStorage.removeItem(c)}}}
function Dw(){if(!Aw())return!1;var a=Cm(),b=Object.keys(window.sessionStorage);b=x(b);for(var c=b.next();!c.done;c=b.next())if(c=Bw(c.value),void 0!==c&&c!==a)return!0;return!1}
;function Ew(){sw().then(function(a){a&&(Jo(a),yw(a),Iu(a),Cw(a))})}
function Fw(){var a=new Oq;Pi.pa(function(){var b,c,d,e,f;return z(function(g){switch(g.h){case 1:if(U("ytidb_clear_optimizations_killswitch")){g.B(2);break}b=Cm("clear");if(b.startsWith("V")&&b.endsWith("||")){var h=[b];Jo(h);yw(h);Iu(h);Cw(h);return g.return()}c=Ju();d=Dw();return g.yield(zw(),3);case 3:return e=g.i,g.yield(Ko(),4);case 4:if(f=g.i,!(c||d||e||f))return g.return();case 2:a.va()?Ew():a.h.add("publicytnetworkstatus-online",Ew,!0,void 0,void 0),g.h=0}})})}
;function Gw(){this.state=1;this.h=null}
m=Gw.prototype;m.initialize=function(a,b,c){if(a.program){var d,e=null!=(d=a.interpreterUrl)?d:null;if(a.interpreterSafeScript){var f=a.interpreterSafeScript;f?((f=f.privateDoNotAccessOrElseSafeScriptWrappedValue)?(d=fb(),f=new ac(d?d.createScript(f):f)):f=null,d=f):d=null}else d=null!=(f=a.interpreterScript)?f:null;a.interpreterSafeUrl&&(e=Dk(a.interpreterSafeUrl).toString());Hw(this,d,e,a.program,b,c)}else bt(Error("Cannot initialize botguard without program"))};
function Hw(a,b,c,d,e,f){var g=void 0===g?"trayride":g;c?(a.state=2,bu(c,function(){window[g]?Iw(a,d,g,e):(a.state=3,du(c),bt(new V("Unable to load Botguard","from "+c)))},f)):b?(f=Gd("SCRIPT"),b instanceof ac?cc(f,b):f.textContent=b,f.nonce=$b(window),document.head.appendChild(f),document.head.removeChild(f),window[g]?Iw(a,d,g,e):(a.state=4,bt(new V("Unable to load Botguard from JS")))):bt(new V("Unable to load VM; no url or JS provided"))}
m.isLoading=function(){return 2===this.state};
function Iw(a,b,c,d){a.state=5;try{var e=new zi({program:b,ge:c,Ge:U("att_web_record_metrics"),Ea:"aGIf"});e.Ze.then(function(){a.state=6;d&&d(b)});
a.Mc(e)}catch(f){a.state=7,f instanceof Error&&bt(f)}}
m.invoke=function(a){a=void 0===a?{}:a;return this.Qc()?this.Fd({Yc:a}):null};
m.dispose=function(){this.Mc(null);this.state=8};
m.Qc=function(){return!!this.h};
m.Fd=function(a){return this.h.zd(a)};
m.Mc=function(a){Cc(this.h);this.h=a};var Jw=[],Kw=!1;function Lw(){if(!U("disable_biscotti_fetch_for_ad_blocker_detection")&&!U("disable_biscotti_fetch_entirely_for_all_web_clients")&&Ft()){var a=T("PLAYER_VARS",{});if("1"!=Pb(a)&&!Gt(a)){var b=function(){Kw=!0;"google_ad_status"in window?bl("DCLKSTAT",1):bl("DCLKSTAT",2)};
try{bu("//static.doubleclick.net/instream/ad_status.js",b)}catch(c){}Jw.push(Pi.pa(function(){if(!(Kw||"google_ad_status"in window)){try{fu("//static.doubleclick.net/instream/ad_status.js",b)}catch(c){}Kw=!0;bl("DCLKSTAT",3)}},5E3))}}}
function Mw(){var a=Number(T("DCLKSTAT",0));return isNaN(a)?0:a}
;function Nw(){var a=E("yt.abuse.playerAttLoader");return a&&["bgvma","bgvmb","bgvmc"].every(function(b){return b in a})?a:null}
;function Ow(){Gw.apply(this,arguments)}
y(Ow,Gw);Ow.prototype.Mc=function(a){var b;null==(b=Nw())||b.bgvma();a?(b={bgvma:a.dispose.bind(a),bgvmb:a.snapshot.bind(a),bgvmc:a.zd.bind(a)},D("yt.abuse.playerAttLoader",b),D("yt.abuse.playerAttLoaderRun",function(c){return a.snapshot(c)})):(D("yt.abuse.playerAttLoader",null),D("yt.abuse.playerAttLoaderRun",null))};
Ow.prototype.Qc=function(){return!!Nw()};
Ow.prototype.Fd=function(a){return Nw().bgvmc(a)};function Pw(a){Vr.call(this,void 0===a?"document_active":a);var b=this;this.l=10;this.h=new Map;this.transitions=[{from:"document_active",to:"document_disposed_preventable",action:this.F},{from:"document_active",to:"document_disposed",action:this.v},{from:"document_disposed_preventable",to:"document_disposed",action:this.v},{from:"document_disposed_preventable",to:"flush_logs",action:this.m},{from:"document_disposed_preventable",to:"document_active",action:this.i},{from:"document_disposed",to:"flush_logs",
action:this.m},{from:"document_disposed",to:"document_active",action:this.i},{from:"document_disposed",to:"document_disposed",action:function(){}},
{from:"flush_logs",to:"document_active",action:this.i}];window.addEventListener("pagehide",function(c){b.transition("document_disposed",{event:c})});
window.addEventListener("beforeunload",function(c){b.transition("document_disposed_preventable",{event:c})})}
y(Pw,Vr);Pw.prototype.F=function(a,b){if(!this.h.get("document_disposed_preventable")){a(null==b?void 0:b.event);var c,d;if((null==b?0:null==(c=b.event)?0:c.defaultPrevented)||(null==b?0:null==(d=b.event)?0:d.returnValue)){b.event.returnValue||(b.event.returnValue=!0);b.event.defaultPrevented||b.event.preventDefault();this.h=new Map;this.transition("document_active");return}}this.h.set("document_disposed_preventable",!0);this.h.get("document_disposed")?this.transition("flush_logs"):this.transition("document_disposed")};
Pw.prototype.v=function(a,b){this.h.get("document_disposed")?this.transition("document_active"):(a(null==b?void 0:b.event),this.h.set("document_disposed",!0),this.transition("flush_logs"))};
Pw.prototype.m=function(a,b){a(null==b?void 0:b.event);this.transition("document_active")};
Pw.prototype.i=function(){this.h=new Map};function Qw(a){Vr.call(this,void 0===a?"document_visibility_unknown":a);var b=this;this.transitions=[{from:"document_visibility_unknown",to:"document_visible",action:this.i},{from:"document_visibility_unknown",to:"document_hidden",action:this.h},{from:"document_visibility_unknown",to:"document_foregrounded",action:this.m},{from:"document_visibility_unknown",to:"document_backgrounded",action:this.v},{from:"document_visible",to:"document_hidden",action:this.h},{from:"document_visible",to:"document_foregrounded",
action:this.m},{from:"document_visible",to:"document_visible",action:this.i},{from:"document_foregrounded",to:"document_visible",action:this.i},{from:"document_foregrounded",to:"document_hidden",action:this.h},{from:"document_foregrounded",to:"document_foregrounded",action:this.m},{from:"document_hidden",to:"document_visible",action:this.i},{from:"document_hidden",to:"document_backgrounded",action:this.v},{from:"document_hidden",to:"document_hidden",action:this.h},{from:"document_backgrounded",to:"document_hidden",
action:this.h},{from:"document_backgrounded",to:"document_backgrounded",action:this.v},{from:"document_backgrounded",to:"document_visible",action:this.i}];document.addEventListener("visibilitychange",function(c){"visible"===document.visibilityState?b.transition("document_visible",{event:c}):b.transition("document_hidden",{event:c})});
U("visibility_lifecycles_dynamic_backgrounding")&&(window.addEventListener("blur",function(c){b.transition("document_backgrounded",{event:c})}),window.addEventListener("focus",function(c){b.transition("document_foregrounded",{event:c})}))}
y(Qw,Vr);Qw.prototype.i=function(a,b){a(null==b?void 0:b.event);U("visibility_lifecycles_dynamic_backgrounding")&&this.transition("document_foregrounded")};
Qw.prototype.h=function(a,b){a(null==b?void 0:b.event);U("visibility_lifecycles_dynamic_backgrounding")&&this.transition("document_backgrounded")};
Qw.prototype.v=function(a,b){a(null==b?void 0:b.event)};
Qw.prototype.m=function(a,b){a(null==b?void 0:b.event)};function Rw(){this.l=new Pw;this.v=new Qw}
Rw.prototype.install=function(){var a=A.apply(0,arguments),b=this;a.forEach(function(c){b.l.install(c)});
a.forEach(function(c){b.v.install(c)})};function Sw(){this.l=[];this.i=new Map;this.h=new Map;this.j=new Set}
Sw.prototype.clickCommand=function(a,b,c){var d=a.clickTrackingParams;c=void 0===c?0:c;if(d)if(c=tt(void 0===c?0:c)){a=this.client;d=new mt({trackingParams:d});var e=void 0;if(U("no_client_ve_attach_unless_shown")){var f=Du(d,c);zu.set(f,!0);Eu(d,c)}e=e||"INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK";f=Cu({cttAuthInfo:vt(c)||void 0},c);d={csn:c,ve:d.getAsJson(),gestureType:e};b&&(d.clientData=b);"UNDEFINED_CSN"===c?Fu("visualElementGestured",f,d):a?Us("visualElementGestured",d,a,f):tn("visualElementGestured",
d,f);b=!0}else b=!1;else b=!1;return b};
Sw.prototype.stateChanged=function(a,b,c){this.visualElementStateChanged(new mt({trackingParams:a}),b,void 0===c?0:c)};
Sw.prototype.visualElementStateChanged=function(a,b,c){c=void 0===c?0:c;if(0===c&&this.j.has(c))this.l.push([a,b]);else{var d=c;d=void 0===d?0:d;c=tt(d);a||(a=(a=qt(void 0===d?0:d))?new mt({veType:a,youtubeData:void 0,jspbYoutubeData:void 0}):null);var e=a;c&&e&&(a=this.client,d=Cu({cttAuthInfo:vt(c)||void 0},c),b={csn:c,ve:e.getAsJson(),clientData:b},"UNDEFINED_CSN"===c?Fu("visualElementStateChanged",d,b):a?Us("visualElementStateChanged",b,a,d):tn("visualElementStateChanged",b,d))}};
function Tw(a,b){if(void 0===b)for(var c=st(),d=0;d<c.length;d++)void 0!==c[d]&&Tw(a,c[d]);else a.i.forEach(function(e,f){(f=a.h.get(f))&&Bu(a.client,b,f,e)}),a.i.clear(),a.h.clear()}
;function Uw(){Rw.call(this);var a={};this.install((a.document_disposed={callback:this.h},a));U("combine_ve_grafts")&&(a={},this.install((a.document_disposed={callback:this.i},a)));a={};this.install((a.flush_logs={callback:this.j},a));U("web_log_cfg_cee_ks")||Em(Vw)}
y(Uw,Rw);Uw.prototype.j=function(){tn("finalPayload",{csn:tt()})};
Uw.prototype.h=function(){ft(gt)};
Uw.prototype.i=function(){var a=Tw;Sw.h||(Sw.h=new Sw);a(Sw.h)};
function Vw(){var a=T("CLIENT_EXPERIMENT_EVENTS");if(a){var b=Ji();a=x(a);for(var c=a.next();!c.done;c=a.next())c=c.value,b(c)&&tn("genericClientExperimentEvent",{eventType:c});delete al.CLIENT_EXPERIMENT_EVENTS}}
;function Ww(){}
function Xw(){var a=E("ytglobal.storage_");a||(a=new Ww,D("ytglobal.storage_",a));return a}
Ww.prototype.estimate=function(){var a,b,c;return z(function(d){a=navigator;return(null==(b=a.storage)?0:b.estimate)?d.return(a.storage.estimate()):(null==(c=a.webkitTemporaryStorage)?0:c.queryUsageAndQuota)?d.return(Yw()):d.return()})};
function Yw(){var a=navigator;return new Promise(function(b,c){var d;null!=(d=a.webkitTemporaryStorage)&&d.queryUsageAndQuota?a.webkitTemporaryStorage.queryUsageAndQuota(function(e,f){b({usage:e,quota:f})},function(e){c(e)}):c(Error("webkitTemporaryStorage is not supported."))})}
D("ytglobal.storageClass_",Ww);function rn(a,b){var c=this;this.handleError=a;this.h=b;this.i=!1;void 0===self.document||self.addEventListener("beforeunload",function(){c.i=!0});
this.j=.2>=Math.random()}
rn.prototype.Ha=function(a){this.handleError(a)};
rn.prototype.logEvent=function(a,b){switch(a){case "IDB_DATA_CORRUPTED":U("idb_data_corrupted_killswitch")||this.h("idbDataCorrupted",b);break;case "IDB_UNEXPECTEDLY_CLOSED":this.h("idbUnexpectedlyClosed",b);break;case "IS_SUPPORTED_COMPLETED":U("idb_is_supported_completed_killswitch")||this.h("idbIsSupportedCompleted",b);break;case "QUOTA_EXCEEDED":Zw(this,b);break;case "TRANSACTION_ENDED":this.j&&.1>=Math.random()&&this.h("idbTransactionEnded",b);break;case "TRANSACTION_UNEXPECTEDLY_ABORTED":a=
Object.assign({},b,{hasWindowUnloaded:this.i}),this.h("idbTransactionAborted",a)}};
function Zw(a,b){Xw().estimate().then(function(c){c=Object.assign({},b,{isSw:void 0===self.document,isIframe:self!==self.top,deviceStorageUsageMbytes:$w(null==c?void 0:c.usage),deviceStorageQuotaMbytes:$w(null==c?void 0:c.quota)});a.h("idbQuotaExceeded",c)})}
function $w(a){return"undefined"===typeof a?"-1":String(Math.ceil(a/1048576))}
;function ax(a,b,c){G.call(this);var d=this;this.channel="widget";this.sessionId=this.h=this.commands=this.l=null;this.targetOrigin="*";this.j=c||T("POST_MESSAGE_ORIGIN")||document.location.protocol+"//"+document.location.hostname;this.i=b||null;this.m=!!a;this.listener=function(e){a:if(!("*"!==d.j&&e.origin!==d.j||d.i&&e.source!==d.i||"string"!==typeof e.data)){try{var f=JSON.parse(e.data)}catch(g){break a}if(!(null==f||d.m&&(d.sessionId&&d.sessionId!==f.id||d.channel&&d.channel!==f.channel))&&f)switch(f.event){case "listening":"null"!==
e.origin&&(d.j=d.targetOrigin=e.origin);d.i=e.source;d.sessionId=f.id;d.h&&(d.h(),d.h=null);break;case "command":d.l&&(!d.commands||0<=Cb(d.commands,f.func))&&d.l(f.func,f.args,e.origin)}}};
window.addEventListener("message",this.listener)}
y(ax,G);ax.prototype.sendMessage=function(a,b){if(b=b||this.i){this.sessionId&&(a.id=this.sessionId);this.channel&&(a.channel=this.channel);try{var c=JSON.stringify(a);b.postMessage(c,this.targetOrigin)}catch(d){bt(d)}}};
ax.prototype.U=function(){window.removeEventListener("message",this.listener);G.prototype.U.call(this)};var bx={},cx=(bx["api.invalidparam"]=2,bx.auth=150,bx["drm.auth"]=150,bx["heartbeat.net"]=150,bx["heartbeat.servererror"]=150,bx["heartbeat.stop"]=150,bx["html5.unsupportedads"]=5,bx["fmt.noneavailable"]=5,bx["fmt.decode"]=5,bx["fmt.unplayable"]=5,bx["html5.missingapi"]=5,bx["html5.unsupportedlive"]=5,bx["drm.unavailable"]=5,bx["mrm.blocked"]=151,bx);var dx=new Set("endSeconds startSeconds mediaContentUrl suggestedQuality videoId rct rctn".split(" "));function ex(a){return(0===a.search("cue")||0===a.search("load"))&&"loadModule"!==a}
function fx(a,b,c){if("string"===typeof a)return{videoId:a,startSeconds:b,suggestedQuality:c};b={};c=x(dx);for(var d=c.next();!d.done;d=c.next())d=d.value,a[d]&&(b[d]=a[d]);return b}
function gx(a,b,c,d){if(Ra(a)&&!Array.isArray(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};"string"===typeof a&&16===a.length?b.list="PL"+a:b.playlist=a;return b}
;function hx(){var a=ix;this.i=[];this.isReady=!1;this.j={};this.listeners=[];this.l=!1;var b=this.h=new ax(!!T("WIDGET_ID_ENFORCE")),c=this.Fe.bind(this);b.l=c;b.commands=null;this.h.channel="widget";if(b=T("WIDGET_ID"))this.h.sessionId=b;this.api=a;this.addEventListener("onReady",this.onReady.bind(this));this.addEventListener("onVideoProgress",this.Ue.bind(this));this.addEventListener("onVolumeChange",this.Ve.bind(this));this.addEventListener("onApiChange",this.Ne.bind(this));this.addEventListener("onPlaybackQualityChange",
this.Re.bind(this));this.addEventListener("onPlaybackRateChange",this.Se.bind(this));this.addEventListener("onStateChange",this.Te.bind(this));this.addEventListener("onWebglSettingsChanged",this.We.bind(this));this.addEventListener("onCaptionsTrackListChanged",this.Oe.bind(this));this.addEventListener("captionssettingschanged",this.Pe.bind(this))}
m=hx.prototype;
m.Fe=function(a,b,c){if("addEventListener"===a&&b)a=b[0],"onReady"===a?this.api.logApiCall(a+" invocation",c):"onError"===a&&this.l&&(this.api.logApiCall(a+" invocation",c,this.errorCode),this.errorCode=void 0),this.api.logApiCall(a+" registration",c),this.j[a]||"onReady"===a||(this.addEventListener(a,jx(this,a,c)),this.j[a]=!0);else if(this.api.isExternalMethodAvailable(a,c)){b=b||[];if(0<b.length&&ex(a)){var d=b;if(Ra(d[0])&&!Array.isArray(d[0]))var e=d[0];else switch(e={},a){case "loadVideoById":case "cueVideoById":e=fx(d[0],
void 0!==d[1]?Number(d[1]):void 0,d[2]);break;case "loadVideoByUrl":case "cueVideoByUrl":e=d[0];"string"===typeof e&&(e={mediaContentUrl:e,startSeconds:void 0!==d[1]?Number(d[1]):void 0,suggestedQuality:d[2]});b:{if((d=e.mediaContentUrl)&&(d=/\/([ve]|embed)\/([^#?]+)/.exec(d))&&d[2]){d=d[2];break b}d=null}e.videoId=d;e=fx(e);break;case "loadPlaylist":case "cuePlaylist":e=gx(d[0],d[1],d[2],d[3])}b.length=1;b[0]=e}this.api.handleExternalCall(a,b,c);ex(a)&&kx(this,lx(this))}};
m.be=function(){this.isReady=!0;this.sendMessage("initialDelivery",lx(this));this.sendMessage("onReady");Db(this.i,this.wd,this);this.i=[]};
function kx(a,b){a.sendMessage("infoDelivery",b)}
m.wd=function(a){this.isReady?this.h.sendMessage(a):this.i.push(a)};
m.sendMessage=function(a,b){this.wd({event:a,info:void 0===b?null:b})};
function jx(a,b,c){return function(d){"onError"===b?a.api.logApiCall(b+" invocation",c,d):a.api.logApiCall(b+" invocation",c);a.sendMessage(b,d)}}
m.onReady=function(){var a=this.h,b=this.be.bind(this);a.h=b;a=this.api.getVideoData();if(!a.isPlayable){this.l=!0;a=a.errorCode;var c=void 0===c?5:c;this.errorCode=a?cx[a]||c:c;this.sendMessage("onError",this.errorCode.toString())}};
m.addEventListener=function(a,b){this.listeners.push({eventType:a,listener:b});this.api.addEventListener(a,b)};
function lx(a){if(!a.api)return null;var b=a.api.getApiInterface();Ib(b,"getVideoData");for(var c={apiInterface:b},d=0,e=b.length;d<e;d++){var f=b[d];if(0===f.search("get")||0===f.search("is")){var g=0;0===f.search("get")?g=3:0===f.search("is")&&(g=2);g=f.charAt(g).toLowerCase()+f.substr(g+1);try{var h=a.api[f]();c[g]=h}catch(k){}}}c.videoData=a.api.getVideoData();c.currentTimeLastUpdated_=Date.now()/1E3;return c}
m.Te=function(a){a={playerState:a,currentTime:this.api.getCurrentTime(),duration:this.api.getDuration(),videoData:this.api.getVideoData(),videoStartBytes:0,videoBytesTotal:this.api.getVideoBytesTotal(),videoLoadedFraction:this.api.getVideoLoadedFraction(),playbackQuality:this.api.getPlaybackQuality(),availableQualityLevels:this.api.getAvailableQualityLevels(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.api.getPlaybackRate(),mediaReferenceTime:this.api.getMediaReferenceTime()};this.api.getVideoUrl&&
(a.videoUrl=this.api.getVideoUrl());this.api.getVideoContentRect&&(a.videoContentRect=this.api.getVideoContentRect());this.api.getProgressState&&(a.progressState=this.api.getProgressState());this.api.getPlaylist&&(a.playlist=this.api.getPlaylist());this.api.getPlaylistIndex&&(a.playlistIndex=this.api.getPlaylistIndex());this.api.getStoryboardFormat&&(a.storyboardFormat=this.api.getStoryboardFormat());kx(this,a)};
m.Re=function(a){a={playbackQuality:a};this.api.getAvailableQualityLevels&&(a.availableQualityLevels=this.api.getAvailableQualityLevels());this.api.getPreferredQuality&&(a.preferredQuality=this.api.getPreferredQuality());kx(this,a)};
m.Se=function(a){kx(this,{playbackRate:a})};
m.Ne=function(){for(var a=this.api.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.api.getOptions(e);a.join(", ");b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var k=f[g],l=this.api.getOption(e,k);b[e][k]=l}}this.sendMessage("apiInfoDelivery",b)};
m.Ve=function(){kx(this,{muted:this.api.isMuted(),volume:this.api.getVolume()})};
m.Ue=function(a){a={currentTime:a,videoBytesLoaded:this.api.getVideoBytesLoaded(),videoLoadedFraction:this.api.getVideoLoadedFraction(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.api.getPlaybackRate(),mediaReferenceTime:this.api.getMediaReferenceTime()};this.api.getProgressState&&(a.progressState=this.api.getProgressState());kx(this,a)};
m.We=function(){var a={sphericalProperties:this.api.getSphericalProperties()};kx(this,a)};
m.Oe=function(){if(this.api.getCaptionTracks){var a={captionTracks:this.api.getCaptionTracks()};kx(this,a)}};
m.Pe=function(){if(this.api.getSubtitlesUserSettings){var a={subtitlesUserSettings:this.api.getSubtitlesUserSettings()};kx(this,a)}};
m.dispose=function(){this.h=null;for(var a=0;a<this.listeners.length;a++){var b=this.listeners[a];this.api.removeEventListener(b.eventType,b.listener)}this.listeners=[]};function mx(a,b){G.call(this);this.h={};this.started=!1;this.connection=b;this.connection.subscribe("command",this.rd,this);this.api=a;this.start()}
y(mx,G);m=mx.prototype;m.start=function(){this.started||this.V||(this.started=!0,this.connection.jb("RECEIVING"))};
m.jb=function(a,b){this.started&&!this.V&&this.connection.jb(a,b)};
m.rd=function(a,b,c){if(this.started&&!this.V){var d=b||{};switch(a){case "addEventListener":"string"===typeof d.event&&this.addListener(d.event);break;case "removeEventListener":"string"===typeof d.event&&this.removeListener(d.event);break;default:this.api.isReady()&&this.api.isExternalMethodAvailable(a,c||null)&&(b=nx(a,b||{}),c=this.api.handleExternalCall(a,b,c||null),(c=ox(a,c))&&this.jb(a,c))}}};
m.addListener=function(a){if(!(a in this.h)){var b=this.Qe.bind(this,a);this.h[a]=b;this.addEventListener(a,b)}};
m.Qe=function(a,b){this.started&&!this.V&&this.connection.jb(a,px(a,b))};
m.removeListener=function(a){a in this.h&&(this.removeEventListener(a,this.h[a]),delete this.h[a])};
m.addEventListener=function(a,b){this.api.addEventListener(a,b)};
m.removeEventListener=function(a,b){this.api.removeEventListener(a,b)};
function nx(a,b){switch(a){case "loadVideoById":return a=fx(b),[a];case "cueVideoById":return a=fx(b),[a];case "loadVideoByPlayerVars":return[b];case "cueVideoByPlayerVars":return[b];case "loadPlaylist":return a=gx(b),[a];case "cuePlaylist":return a=gx(b),[a];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];case "setLoop":return[b.loopPlaylists];
case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey,b.ctrlKey,b.altKey,b.metaKey,b.key,b.code]}return[]}
function ox(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
function px(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}if(null!=b)return{value:b}}
m.U=function(){this.connection.unsubscribe("command",this.rd,this);this.connection=null;for(var a in this.h)this.h.hasOwnProperty(a)&&this.removeListener(a);G.prototype.U.call(this);delete this.api};function qx(a,b,c){qu.call(this);this.j=a;this.i=b;this.id=c}
y(qx,qu);qx.prototype.jb=function(a,b){this.V||this.j.jb(this.i,this.id,a,b)};
qx.prototype.U=function(){this.i=this.j=null;qu.prototype.U.call(this)};function rx(a,b,c){G.call(this);this.h=a;this.origin=c;this.j=ir(window,"message",this.i.bind(this));this.connection=new qx(this,a,b);Ec(this,this.connection)}
y(rx,G);rx.prototype.jb=function(a,b,c,d){this.V||a!==this.h||(a={id:b,command:c},d&&(a.data=d),this.h.postMessage(JSON.stringify(a),this.origin))};
rx.prototype.i=function(a){if(!this.V&&a.origin===this.origin){var b=a.data;if("string"===typeof b){try{b=JSON.parse(b)}catch(d){return}if(b.command){var c=this.connection;c.V||c.l("command",b.command,b.data,a.origin)}}}};
rx.prototype.U=function(){kr(this.j);this.h=null;G.prototype.U.call(this)};var sx=new Ow;function tx(){return sx.Qc()}
function ux(a){a=void 0===a?{}:a;return sx.invoke(a)}
;function vx(a,b,c,d,e){G.call(this);var f=this;this.A=b;this.webPlayerContextConfig=d;this.uc=e;this.Za=!1;this.api={};this.ja=this.m=null;this.W=new M;this.h={};this.da=this.xa=this.elementId=this.Cb=this.config=null;this.ba=!1;this.j=this.F=null;this.Ga={};this.vc=["onReady"];this.lastError=null;this.Ub=NaN;this.K={};this.ga=0;this.i=this.l=a;Ec(this,this.W);wx(this);c?this.ga=setTimeout(function(){f.loadNewVideoConfig(c)},0):d&&(xx(this),yx(this))}
y(vx,G);m=vx.prototype;m.getId=function(){return this.A};
m.loadNewVideoConfig=function(a){if(!this.V){this.ga&&(clearTimeout(this.ga),this.ga=0);var b=a||{};b instanceof Tt||(b=new Tt(b));this.config=b;this.setConfig(a);yx(this);this.isReady()&&zx(this)}};
function xx(a){var b;a.webPlayerContextConfig?b=a.webPlayerContextConfig.rootElementId:b=a.config.attrs.id;a.elementId=b||a.elementId;"video-player"===a.elementId&&(a.elementId=a.A,a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.A:a.config.attrs.id=a.A);var c;(null==(c=a.i)?void 0:c.id)===a.elementId&&(a.elementId+="-player",a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.elementId:a.config.attrs.id=a.elementId)}
m.setConfig=function(a){this.Cb=a;this.config=Ax(a);xx(this);if(!this.xa){var b;this.xa=Bx(this,(null==(b=this.config.args)?void 0:b.jsapicallback)||"onYouTubePlayerReady")}this.config.args?this.config.args.jsapicallback=null:this.config.args={jsapicallback:null};var c;if(null==(c=this.config)?0:c.attrs)a=this.config.attrs,(b=a.width)&&this.i&&(this.i.style.width=Hi(Number(b)||b)),(a=a.height)&&this.i&&(this.i.style.height=Hi(Number(a)||a))};
function zx(a){if(a.config&&!0!==a.config.loaded)if(a.config.loaded=!0,!a.config.args||"0"!==a.config.args.autoplay&&0!==a.config.args.autoplay&&!1!==a.config.args.autoplay){var b;a.api.loadVideoByPlayerVars(null!=(b=a.config.args)?b:null)}else a.api.cueVideoByPlayerVars(a.config.args)}
function Cx(a){var b=!0,c=Dx(a);c&&a.config&&(b=c.dataset.version===Ex(a));return b&&!!E("yt.player.Application.create")}
function yx(a){if(!a.V&&!a.ba){var b=Cx(a);if(b&&"html5"===(Dx(a)?"html5":null))a.da="html5",a.isReady()||Fx(a);else if(Gx(a),a.da="html5",b&&a.j&&a.l)a.l.appendChild(a.j),Fx(a);else{a.config&&(a.config.loaded=!0);var c=!1;a.F=function(){c=!0;var d=Hx(a,"player_bootstrap_method")?E("yt.player.Application.createAlternate")||E("yt.player.Application.create"):E("yt.player.Application.create");var e=a.config?Ax(a.config):void 0;d&&d(a.l,e,a.webPlayerContextConfig,a.uc);Fx(a)};
a.ba=!0;b?a.F():(bu(Ex(a),a.F),(b=Ix(a))&&iu(b||""),Jx(a)&&!c&&D("yt.player.Application.create",null))}}}
function Dx(a){var b=Fd(a.elementId);!b&&a.i&&a.i.querySelector&&(b=a.i.querySelector("#"+a.elementId));return b}
function Fx(a){if(!a.V){var b=Dx(a),c=!1;b&&b.getApiInterface&&b.getApiInterface()&&(c=!0);if(c){a.ba=!1;if(!Hx(a,"html5_remove_not_servable_check_killswitch")){var d;if((null==b?0:b.isNotServable)&&a.config&&(null==b?0:b.isNotServable(null==(d=a.config.args)?void 0:d.video_id)))return}Kx(a)}else a.Ub=setTimeout(function(){Fx(a)},50)}}
function Kx(a){wx(a);a.Za=!0;var b=Dx(a);if(b){a.m=Lx(a,b,"addEventListener");a.ja=Lx(a,b,"removeEventListener");var c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());for(var d=a.api,e=0;e<c.length;e++){var f=c[e];d[f]||(d[f]=Lx(a,b,f))}}for(var g in a.h)a.h.hasOwnProperty(g)&&a.m&&a.m(g,a.h[g]);zx(a);a.xa&&a.xa(a.api);a.W.Ya("onReady",a.api)}
function Lx(a,b,c){var d=b[c];return function(){var e=A.apply(0,arguments);try{return a.lastError=null,d.apply(b,e)}catch(f){if("sendAbandonmentPing"!==c)throw f.params=c,a.lastError=f,e=new V("PlayerProxy error in method call",{error:f,method:c,playerId:a.A}),e.level="WARNING",e;}}}
function wx(a){a.Za=!1;if(a.ja)for(var b in a.h)a.h.hasOwnProperty(b)&&a.ja(b,a.h[b]);for(var c in a.K)a.K.hasOwnProperty(c)&&clearTimeout(Number(c));a.K={};a.m=null;a.ja=null;b=a.api;for(var d in b)b.hasOwnProperty(d)&&(b[d]=null);b.addEventListener=function(e,f){a.addEventListener(e,f)};
b.removeEventListener=function(e,f){a.removeEventListener(e,f)};
b.destroy=function(){a.dispose()};
b.getLastError=function(){return a.getLastError()};
b.getPlayerType=function(){return a.getPlayerType()};
b.getCurrentVideoConfig=function(){return a.Cb};
b.loadNewVideoConfig=function(e){a.loadNewVideoConfig(e)};
b.isReady=function(){return a.isReady()}}
m.isReady=function(){return this.Za};
m.addEventListener=function(a,b){var c=this,d=Bx(this,b);d&&(0<=Cb(this.vc,a)||this.h[a]||(b=Mx(this,a),this.m&&this.m(a,b)),this.W.subscribe(a,d),"onReady"===a&&this.isReady()&&setTimeout(function(){d(c.api)},0))};
m.removeEventListener=function(a,b){this.V||(b=Bx(this,b))&&this.W.unsubscribe(a,b)};
function Bx(a,b){var c=b;if("string"===typeof b){if(a.Ga[b])return a.Ga[b];c=function(){var d=A.apply(0,arguments),e=E(b);if(e)try{e.apply(B,d)}catch(f){throw d=new V("PlayerProxy error when executing callback",{error:f}),d.level="ERROR",d;}};
a.Ga[b]=c}return c?c:null}
function Mx(a,b){function c(d){var e=setTimeout(function(){if(!a.V){try{a.W.Ya(b,null!=d?d:void 0)}catch(h){var f=new V("PlayerProxy error when creating global callback",{error:h.message,event:b,playerId:a.A,data:d,originalStack:h.stack});f.level="WARNING";throw f;}f=a.K;var g=String(e);g in f&&delete f[g]}},0);
Ob(a.K,String(e))}
return a.h[b]=c}
m.getPlayerType=function(){return this.da||(Dx(this)?"html5":null)};
m.getLastError=function(){return this.lastError};
function Gx(a){a.cancel();wx(a);a.da=null;a.config&&(a.config.loaded=!1);var b=Dx(a);b&&(Cx(a)||!Jx(a)?a.j=b:(b&&b.destroy&&b.destroy(),a.j=null));if(a.l)for(a=a.l;b=a.firstChild;)a.removeChild(b)}
m.cancel=function(){this.F&&fu(Ex(this),this.F);clearTimeout(this.Ub);this.ba=!1};
m.U=function(){Gx(this);if(this.j&&this.config&&this.j.destroy)try{this.j.destroy()}catch(b){var a=new V("PlayerProxy error during disposal",{error:b});a.level="ERROR";throw a;}this.Ga=null;for(a in this.h)this.h.hasOwnProperty(a)&&delete this.h[a];this.Cb=this.config=this.api=null;delete this.l;delete this.i;G.prototype.U.call(this)};
function Jx(a){var b,c;a=null==(b=a.config)?void 0:null==(c=b.args)?void 0:c.fflags;return!!a&&-1!==a.indexOf("player_destroy_old_version=true")}
function Ex(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.jsUrl:(a=a.config.assets)?a.js:""}
function Ix(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.cssUrl:(a=a.config.assets)?a.css:""}
function Hx(a,b){if(a.webPlayerContextConfig)var c=a.webPlayerContextConfig.serializedExperimentFlags;else{var d;if(null==(d=a.config)?0:d.args)c=a.config.args.fflags}return(c||"").split("&").includes(b+"=true")}
function Ax(a){for(var b={},c=x(Object.keys(a)),d=c.next();!d.done;d=c.next()){d=d.value;var e=a[d];b[d]="object"===typeof e?Rb(e):e}return b}
;var Nx={},Ox="player_uid_"+(1E9*Math.random()>>>0);function Px(a,b){var c="player",d=!1;d=void 0===d?!0:d;c="string"===typeof c?Fd(c):c;var e=Ox+"_"+Sa(c),f=Nx[e];if(f&&d)return Qx(a,b)?f.api.loadVideoByPlayerVars(a.args||null):f.loadNewVideoConfig(a),f.api;f=new vx(c,e,a,b,void 0);Nx[e]=f;f.addOnDisposeCallback(function(){delete Nx[f.getId()]});
return f.api}
function Qx(a,b){return b&&b.serializedExperimentFlags?b.serializedExperimentFlags.includes("web_player_remove_playerproxy=true"):a&&a.args&&a.args.fflags?a.args.fflags.includes("web_player_remove_playerproxy=true"):!1}
;var ix=null,Rx=null,Sx=null;
function Tx(){Vv();var a=qm(),b=tm(119),c=1<window.devicePixelRatio;if(document.body&&Xi(document.body,"exp-invert-logo"))if(c&&!Xi(document.body,"inverted-hdpi")){var d=document.body;if(d.classList)d.classList.add("inverted-hdpi");else if(!Xi(d,"inverted-hdpi")){var e=Vi(d);Wi(d,e+(0<e.length?" inverted-hdpi":"inverted-hdpi"))}}else!c&&Xi(document.body,"inverted-hdpi")&&Yi();if(b!=c){b="f"+(Math.floor(119/31)+1);d=um(b)||0;d=c?d|67108864:d&-67108865;0===d?delete nm[b]:(c=d.toString(16),nm[b]=c.toString());
c=!0;U("web_secure_pref_cookie_killswitch")&&(c=!1);b=a.h;d=[];for(f in nm)nm.hasOwnProperty(f)&&d.push(f+"="+encodeURIComponent(String(nm[f])));var f=d.join("&");jm(b,f,63072E3,a.i,c)}}
function Ux(){Vx()}
function Wx(){Uv("ep_init_pr");Vx()}
function Vx(){var a=ix.getVideoData(1);a=a.title?a.title+" - YouTube":"YouTube";document.title!==a&&(document.title=a)}
function Xx(){ix&&ix.sendAbandonmentPing&&ix.sendAbandonmentPing();T("PL_ATT")&&sx.dispose();for(var a=Pi,b=0,c=Jw.length;b<c;b++)a.qa(Jw[b]);Jw.length=0;du("//static.doubleclick.net/instream/ad_status.js");Kw=!1;bl("DCLKSTAT",0);Dc(Sx,Rx);ix&&(ix.removeEventListener("onVideoDataChange",Ux),ix.destroy())}
;D("yt.setConfig",bl);D("yt.config.set",bl);D("yt.setMsg",au);D("yt.msgs.set",au);D("yt.logging.errors.log",at);
D("writeEmbed",function(){var a=T("PLAYER_CONFIG");if(!a){var b=T("PLAYER_VARS");b&&(a={args:b})}Nu(!0);"gvn"===a.args.ps&&(document.body.style.backgroundColor="transparent");a.attrs||(a.attrs={width:"100%",height:"100%",id:"video-player"});var c=document.referrer;b=T("POST_MESSAGE_ORIGIN");window!==window.top&&c&&c!==document.URL&&(a.args.loaderUrl=c);Qv("embed",["ol"]);c=tw();if(!c.serializedForcedExperimentIds){var d=pl(window.location.href);d.forced_experiments&&(c.serializedForcedExperimentIds=
d.forced_experiments)}var e;(null==(e=a.args)?0:e.autoplay)&&Qv("watch",["pbs","pbu","pbp"]);ix=Px(a,c);ix.addEventListener("onVideoDataChange",Ux);ix.addEventListener("onReady",Wx);a=T("POST_MESSAGE_ID","player");T("ENABLE_JS_API")?Sx=new hx:T("ENABLE_POST_API")&&"string"===typeof a&&"string"===typeof b&&(Rx=new rx(window.parent,a,b),Sx=new mx(ix,Rx.connection));Lw();U("ytidb_create_logger_embed_killswitch")||qn();a={};Uw.h||(Uw.h=new Uw);Uw.h.install((a.flush_logs={callback:function(){Hs()}},a));
$q();U("ytidb_clear_embedded_player")&&Pi.pa(function(){var f,g;if(!rw){var h=Mr();Ir(h,{oc:qw,Cd:ow});var k={Xc:{feedbackEndpoint:$u(iw),modifyChannelNotificationPreferenceEndpoint:$u(jw),playlistEditEndpoint:$u(kw),subscribeEndpoint:$u(gw),unsubscribeEndpoint:$u(hw),webPlayerShareEntityServiceEndpoint:$u(lw)}},l=Wu(),n={};l&&(n.client_location=l);void 0===f&&(f=gm());void 0===g&&(g=h.resolve(qw));$v(k,g,f,n);Ir(h,{oc:fw,Dd:Zv.h});rw=h.resolve(fw)}Fw()})});
D("yt.abuse.player.botguardInitialized",E("yt.abuse.player.botguardInitialized")||tx);D("yt.abuse.player.invokeBotguard",E("yt.abuse.player.invokeBotguard")||ux);D("yt.abuse.dclkstatus.checkDclkStatus",E("yt.abuse.dclkstatus.checkDclkStatus")||Mw);D("yt.player.exports.navigate",E("yt.player.exports.navigate")||Mu);D("yt.util.activity.init",E("yt.util.activity.init")||nr);D("yt.util.activity.getTimeSinceActive",E("yt.util.activity.getTimeSinceActive")||qr);
D("yt.util.activity.setTimestamp",E("yt.util.activity.setTimestamp")||or);window.addEventListener("load",fl(function(){Tx()}));
window.addEventListener("pageshow",fl(function(a){a.persisted||Tx()}));
window.addEventListener("pagehide",fl(function(a){U("embeds_web_enable_dispose_player_if_page_not_cached_killswitch")?Xx():a.persisted||Xx()}));
window.onerror=function(a,b,c,d,e){b=void 0===b?"Unknown file":b;c=void 0===c?0:c;var f=!1,g=cl("log_window_onerror_fraction");if(g&&Math.random()<g)f=!0;else{g=document.getElementsByTagName("script");for(var h=0,k=g.length;h<k;h++)if(0<g[h].src.indexOf("/debug-")){f=!0;break}}f&&(f=!1,e?f=!0:("string"===typeof a?g=a:ErrorEvent&&a instanceof ErrorEvent?(f=!0,g=a.message,b=a.filename,c=a.lineno,d=a.colno):(g="Unknown error",b="Unknown file",c=0),e=new V(g),e.name="UnhandledWindowError",e.message=g,
e.fileName=b,e.lineNumber=c,isNaN(d)?delete e.columnNumber:e.columnNumber=d),f?at(e):bt(e))};
je=ct;window.addEventListener("unhandledrejection",function(a){ct(a.reason)});
Db(T("ERRORS")||[],function(a){at.apply(null,a)});
bl("ERRORS",[]);}).call(this);
