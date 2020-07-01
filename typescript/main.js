"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
exports.__esModule = true;
var name = 'Tanmay';
var message = "My name is " + name;
// Two ways to declare type - array
var list1 = [1, 2, 4];
var list2 = ['a', 'b', 'c'];
// Fixed number of values with fix order - tuple
var tuple = ['chris', 22];
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));
;
var c = Color.Green;
console.log(c);
// Woudl print 1
var Color2;
(function (Color2) {
    Color2[Color2["Red"] = 5] = "Red";
    Color2[Color2["Green"] = 6] = "Green";
    Color2[Color2["Blue"] = 7] = "Blue";
})(Color2 || (Color2 = {}));
;
var d = Color2.Green;
console.log(d);
// Woudl print 6
console.log(message);
// If uncertain about the type (e.g. coming from third party) - use any
var randomVal = 10;
randomVal = true;
randomVal = 'Test';
// Any allows doesn't complain on anything - Not even on property assignment nor 
// calling them nor on construting them
// To resolve this - there's more restrictive unknown type
var myval = 10;
// Would complain on following operations
// console.log(myval.name)
// myval()
// myval.toUpperCase()
// To resolve this, we need to do type-asserstion
myval.toUpperCase();
// Even for the custom type
function hasName(obj) {
    return !!obj &&
        typeof obj === 'object' &&
        'name' in obj;
}
if (hasName(myval)) {
    console.log(myval.name);
}
// Type inference from initialization
var a;
a = true;
a = 'Test';
// Would work
// following would not
// let b = 'test2';
// b = true;
// Multi type var
var multiTypeVar;
multiTypeVar = 20;
multiTypeVar = false;
// Functions
function add(num1, num2) {
    if (num2 === void 0) { num2 = 10; }
    return num1 + num2;
}
add(5, 2);
function fullName(person) {
    console.log(person.firstName + ", " + person.lastName);
}
var p = {
    firstName: 'test',
    lastName: 'user'
};
// Class provides ability similar to JAVA of inheritance
var E = /** @class */ (function () {
    function E(name) {
        this.eName = name;
    }
    E.prototype.greet = function () {
        console.log("Hello " + this.eName);
    };
    return E;
}());
var emp1 = new E('testuser');
var M = /** @class */ (function (_super) {
    __extends(M, _super);
    function M(mName) {
        return _super.call(this, mName) || this;
    }
    M.prototype.delegateWork = function () {
        console.log('delegating task');
    };
    return M;
}(E));
var m1 = new M('testuser');
m1.delegateWork();
m1.greet();
// Following will not work as eName in E class is declared as private
// console.log(m1.eName);
