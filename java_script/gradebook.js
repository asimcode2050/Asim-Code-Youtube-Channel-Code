class Student {
    constructor(name) {
        this.name = name;
        this.grades = [];
    }

    addGrade(grade) {
        this.grades.push(grade);
    }

    getAverageGrade() {
        let total = this.grades.reduce((sum, grade) => sum + grade, 0);
        return total / this.grades.length;
    }
}
let gradebook = [];

function addStudent(name) {
    let newStudent = new Student(name);
    gradebook.push(newStudent);
}
function addGradeForStudent(name, grade) {
    let student = gradebook.find(s => s.name === name);
    if (student) {
        student.addGrade(grade);
    } else {
        console.log("Student not found!");
    }
}
function showStudentAverages() {
    gradebook.forEach(student => {
        console.log(`${student.name}: Average Grade = ${student.getAverageGrade().toFixed(2)}`);
    });
}
addStudent("John");
addStudent("Jane");
addGradeForStudent("John", 90);
addGradeForStudent("John", 80);
addGradeForStudent("Jane", 85);
addGradeForStudent("Jane", 95);
showStudentAverages();
