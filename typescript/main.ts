export {}
let name:string = 'Tanmay';

let message = `My name is ${name}`;

// Two ways to declare type - array
let list1: number[] = [1,2,4];
let list2: Array<string> = ['a','b','c'];

// Fixed number of values with fix order - tuple
let tuple: [string, number] = ['chris', 22];

enum Color {Red, Green, Blue};

let c: Color = Color.Green;

console.log(c);
// Woudl print 1

enum Color2 {Red = 5, Green, Blue};

let d: Color2 = Color2.Green;

console.log(d);
// Woudl print 6

console.log(message);

// If uncertain about the type (e.g. coming from third party) - use any

let randomVal: any = 10;
randomVal = true;
randomVal = 'Test';

// Any allows doesn't complain on anything - Not even on property assignment nor 
// calling them nor on construting them

// To resolve this - there's more restrictive unknown type

let myval: unknown = 10;

// Would complain on following operations
// console.log(myval.name)
// myval()
// myval.toUpperCase()

// To resolve this, we need to do type-asserstion

(myval as string).toUpperCase();

// Even for the custom type

function hasName(obj: any): obj is {name: string} {
	return !!obj && 
	typeof obj === 'object' &&
	'name' in obj
	}

if (hasName(myval)){
	console.log(myval.name);
}


// Type inference from initialization

let a;
a = true;
a = 'Test';

// Would work

// following would not

// let b = 'test2';
// b = true;


// Multi type var

let multiTypeVar: boolean | number;
multiTypeVar = 20;
multiTypeVar = false;



// Functions

function add (num1: number, num2: number = 10): number {
	return num1 + num2;
	}

add(5,2)
// add(5,'name')



// Interface

interface Person {
	firstName: string,
	lastName?: string // Use ? for optional field
	}

function fullName(person: Person) {
	console.log(`${person.firstName}, ${person.lastName}`);
	}

let p = {
	firstName: 'test',
	lastName: 'user'
	}

// Class provides ability similar to JAVA of inheritance

class E {
	private eName: string;

	constructor(name: string) {
		this.eName = name;
	}
	
	greet() {
		console.log(`Hello ${this.eName}`);
	}
}

let emp1 = new E('testuser');

class M extends E {
	constructor(mName: string) {
		super(mName);
	}	
	
	delegateWork() {
		console.log('delegating task');
	}
}

let m1 = new M('testuser');
m1.delegateWork()
m1.greet();
// Following will not work as eName in E class is declared as private
// console.log(m1.eName);




