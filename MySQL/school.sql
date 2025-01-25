-- Step 1: Create the database
CREATE DATABASE IF NOT EXISTS school_management;
USE school_management;

-- Step 2: Create the Students table
CREATE TABLE IF NOT EXISTS Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    address VARCHAR(255),
    contact_number VARCHAR(15),
    other_student_details TEXT
);

-- Step 3: Insert sample data into the Students table
INSERT INTO Students (first_name, last_name, date_of_birth, gender, address, contact_number, other_student_details)
VALUES 
('John', 'Doe', '2010-05-15', 'Male', '123 Main St, Springfield', '123-456-7890', 'Excellent in Mathematics'),
('Jane', 'Smith', '2011-08-22', 'Female', '456 Elm St, Shelbyville', '234-567-8901', 'Loves Science');

-- Step 4: Create the Teachers table
CREATE TABLE IF NOT EXISTS Teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    address VARCHAR(255),
    contact_number VARCHAR(15),
    other_teacher_details TEXT
);

-- Step 5: Insert sample data into the Teachers table
INSERT INTO Teachers (first_name, last_name, date_of_birth, gender, address, contact_number, other_teacher_details)
VALUES 
('Robert', 'Brown', '1980-03-10', 'Male', '789 Oak St, Springfield', '345-678-9012', 'Math Teacher'),
('Emily', 'White', '1985-07-20', 'Female', '321 Pine St, Shelbyville', '456-789-0123', 'Science Teacher');

-- Step 6: Create the Classes table
CREATE TABLE IF NOT EXISTS Classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(255) NOT NULL,
    teacher_id INT,
    other_class_details TEXT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

-- Step 7: Insert sample data into the Classes table
INSERT INTO Classes (class_name, teacher_id, other_class_details)
VALUES 
('Math', 1, 'Advanced Mathematics'),
('Science', 2, 'General Science');

-- Step 8: Create the Subjects table
CREATE TABLE IF NOT EXISTS Subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(255) NOT NULL,
    class_id INT,
    other_subject_details TEXT,
    FOREIGN KEY (class_id) REFERENCES Classes(class_id)
);

-- Step 9: Insert sample data into the Subjects table
INSERT INTO Subjects (subject_name, class_id, other_subject_details)
VALUES 
('Algebra', 1, 'Basic Algebra'),
('Biology', 2, 'Introduction to Biology');

-- Step 10: Create the Enrollments table
CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    class_id INT,
    enrollment_date DATE NOT NULL,
    other_enrollment_details TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (class_id) REFERENCES Classes(class_id)
);

-- Step 11: Insert sample data into the Enrollments table
INSERT INTO Enrollments (student_id, class_id, enrollment_date, other_enrollment_details)
VALUES 
(1, 1, '2023-09-01', 'Enrolled in Math'),
(2, 2, '2023-09-01', 'Enrolled in Science');

-- Step 12: Create the Grades table
CREATE TABLE IF NOT EXISTS Grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    grade VARCHAR(2) NOT NULL,
    grade_date DATE NOT NULL,
    other_grade_details TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);

-- Step 13: Insert sample data into the Grades table
INSERT INTO Grades (student_id, subject_id, grade, grade_date, other_grade_details)
VALUES 
(1, 1, 'A', '2023-10-15', 'Excellent performance in Algebra'),
(2, 2, 'B', '2023-10-15', 'Good performance in Biology');

-- Step 14: Query to display all tables as a single view
SELECT 'Students' AS Table_Name, student_id AS ID, first_name AS Column1, last_name AS Column2, date_of_birth AS Column3, gender AS Column4, address AS Column5, contact_number AS Column6, other_student_details AS Column7, NULL AS Column8, NULL AS Column9, NULL AS Column10 FROM Students
UNION ALL
SELECT 'Teachers', teacher_id, first_name, last_name, date_of_birth, gender, address, contact_number, other_teacher_details, NULL, NULL, NULL FROM Teachers
UNION ALL
SELECT 'Classes', class_id, class_name, teacher_id, NULL, NULL, NULL, NULL, other_class_details, NULL, NULL, NULL FROM Classes
UNION ALL
SELECT 'Subjects', subject_id, subject_name, class_id, NULL, NULL, NULL, NULL, other_subject_details, NULL, NULL, NULL FROM Subjects
UNION ALL
SELECT 'Enrollments', enrollment_id, student_id, class_id, enrollment_date, NULL, NULL, NULL, other_enrollment_details, NULL, NULL, NULL FROM Enrollments
UNION ALL
SELECT 'Grades', grade_id, student_id, subject_id, grade, grade_date, NULL, NULL, other_grade_details, NULL, NULL, NULL FROM Grades;

-- Step 15: Example of an UPDATE query
UPDATE Students
SET contact_number = '111-222-3333'
WHERE student_id = 1;

-- Step 16: Example of a DELETE query
DELETE FROM Grades
WHERE grade_id = 2;

-- Step 17: Example of a SELECT query with JOIN
SELECT 
    s.first_name, 
    s.last_name, 
    c.class_name, 
    sub.subject_name, 
    g.grade
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Classes c ON e.class_id = c.class_id
JOIN Subjects sub ON c.class_id = sub.class_id
JOIN Grades g ON s.student_id = g.student_id AND sub.subject_id = g.subject_id;

-- Step 18: Example of a SELECT query with WHERE clause
SELECT *
FROM Teachers
WHERE gender = 'Female';

-- Step 19: Example of a SELECT query with ORDER BY
SELECT *
FROM Students
ORDER BY date_of_birth DESC;

-- Step 20: Example of a SELECT query with GROUP BY
SELECT 
    class_id, 
    COUNT(student_id) AS total_students
FROM Enrollments
GROUP BY class_id;
