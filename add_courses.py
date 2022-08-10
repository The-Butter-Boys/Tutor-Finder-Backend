# Script to add UNO's CSCI courses to the database


from tutor_finder import db
from tutor_finder.models import Course

courses = [
	{'department': 'CSCI', 'number': '1200', 'name': 'COMPUTER SCIENCE PRINCIPLES'},
	{'department': 'CSCI', 'number': '1204', 'name': 'COMPUTER SCIENCE PRINCIPLES LABORATORY'},
	{'department': 'CSCI', 'number': '1280', 'name': 'INTRODUCTION TO COMPUTATIONAL SCIENCE'},
	{'department': 'CSCI', 'number': '1620', 'name': 'INTRODUCTION TO COMPUTER SCIENCE II'},
	{'department': 'CSCI', 'number': '2030', 'name': 'MATHEMATICAL FOUNDATIONS OF COMPUTER SCIENCE'},
	{'department': 'CSCI', 'number': '2240', 'name': 'INTRODUCTION TO C PROGRAMMING'},
	{'department': 'CSCI', 'number': '2410', 'name': 'INTRODUCTION TO DATA ANALYTICS USING PYTHON'},
	{'department': 'CSCI', 'number': '2510', 'name': 'INTRODUCTION TO GAME PROGRAMMING'},
	{'department': 'CSCI', 'number': '2620', 'name': '2D GRAPHICS: IMAGE PROCESSING'},
	{'department': 'CSCI', 'number': '2830', 'name': 'OBJECT-ORIENTED SOFTWARE ENGINEERING FUNDAMENTALS'},
	{'department': 'CSCI', 'number': '2840', 'name': 'C++ & OBJECT-ORIENTED PROGRAMMING'},
	{'department': 'CSCI', 'number': '2850', 'name': 'PROGRAMMING ON THE INTERNET'},
	{'department': 'CSCI', 'number': '2960', 'name': 'SHORT TOPICS FOR PROGRAMMERS'},
	{'department': 'CSCI', 'number': '2980', 'name': 'TOPICS IN COMPUTER SCIENCE'},
	{'department': 'CSCI', 'number': '3100', 'name': 'APPLIED COMBINATORICS'},
	{'department': 'CSCI', 'number': '3300', 'name': 'NUMERICAL METHODS'},
	{'department': 'CSCI', 'number': '3320', 'name': 'DATA STRUCTURES'},
	{'department': 'CSCI', 'number': '3450', 'name': 'NATURAL LANGUAGE PROCESSING'},
	{'department': 'CSCI', 'number': '3470', 'name': 'FUNDAMENTALS AND ALGORITHMS OF MACHINE LEARNING'},
	{'department': 'CSCI', 'number': '3510', 'name': 'ADVANCED GAME PROGRAMMING'},
	{'department': 'CSCI', 'number': '3550', 'name': 'COMMUNICATION NETWORKS'},
	{'department': 'CSCI', 'number': '3660', 'name': 'THEORY OF COMPUTATION'},
	{'department': 'CSCI', 'number': '3710', 'name': 'INTRODUCTION TO DIGITAL DESIGN AND COMPUTER ORGANIZATION'},
	{'department': 'CSCI', 'number': '3830', 'name': 'ADVANCED JAVA PROGRAMMING'},
	{'department': 'CSCI', 'number': '3850', 'name': 'FOUNDATIONS OF WEB SEARCH TECHNOLOGIES'},
	{'department': 'CSCI', 'number': '4010', 'name': 'INTRODUCTION TO THE THEORY OF RECURSIVE FUNCTIONS'},
	{'department': 'CSCI', 'number': '4100', 'name': 'INTRODUCTION TO ALGORITHMS'},
	{'department': 'CSCI', 'number': '4150', 'name': 'GRAPH THEORY & APPLICATIONS'},
	{'department': 'CSCI', 'number': '4220', 'name': 'PRINCIPLES OF PROGRAMMING LANGUAGES'},
	{'department': 'CSCI', 'number': '4250', 'name': 'HUMAN COMPUTER INTERACTION'},
	{'department': 'CSCI', 'number': '4260', 'name': 'USER EXPERIENCE DESIGN'},
	{'department': 'CSCI', 'number': '4300', 'name': 'DETERMINISTIC OPERATIONS RESEARCH MODELS'},
	{'department': 'CSCI', 'number': '4310', 'name': 'PROBABILISTIC OPERATIONS RESEARCH MODELS'},
	{'department': 'CSCI', 'number': '4350', 'name': 'COMPUTER ARCHITECTURE'},
	{'department': 'CSCI', 'number': '4380', 'name': 'DIGITAL FORENSICS'},
	{'department': 'CSCI', 'number': '4430', 'name': 'QUANTUM COMPUTING AND CRYPTOGRAPHY'},
	{'department': 'CSCI', 'number': '4440', 'name': 'INTRODUCTION TO PARALLEL COMPUTING'},
	{'department': 'CSCI', 'number': '4450', 'name': 'INTRODUCTION TO ARTIFICIAL INTELLIGENCE'},
	{'department': 'CSCI', 'number': '4470', 'name': 'PATTERN RECOGNITION'},
	{'department': 'CSCI', 'number': '4480', 'name': 'ALGORITHMS FOR ROBOTICS'},
	{'department': 'CSCI', 'number': '4500', 'name': 'OPERATING SYSTEMS'},
	{'department': 'CSCI', 'number': '4560', 'name': 'NUMBER THEORY & CRYPTOGRAPHY'},
	{'department': 'CSCI', 'number': '4620', 'name': 'COMPUTER GRAPHICS'},
	{'department': 'CSCI', 'number': '4660', 'name': 'AUTOMATA, COMPUTABILITY, AND FORMAL LANGUAGES'},
	{'department': 'CSCI', 'number': '4700', 'name': 'COMPILER CONSTRUCTION'},
	{'department': 'CSCI', 'number': '4760', 'name': 'TOPICS IN MODELING'},
	{'department': 'CSCI', 'number': '4830', 'name': 'INTRODUCTION SOFTWARE ENGINEERING'},
	{'department': 'CSCI', 'number': '4850', 'name': 'DATABASE MANAGEMENT SYSTEMS'},
	{'department': 'CSCI', 'number': '4890', 'name': 'DATA WAREHOUSING AND DATA MINING'},
	{'department': 'CSCI', 'number': '4900', 'name': 'INTERNET SYSTEMS DEVELOPMENT'},
	{'department': 'CSCI', 'number': '4950', 'name': 'INTERNSHIP IN COMPUTER SCIENCE'},
	{'department': 'CSCI', 'number': '4970', 'name': 'CAPSTONE PROJECT'},
	{'department': 'CSCI', 'number': '4980', 'name': 'TOPICS IN COMPUTER SCIENCE'}
]

for course in courses:
	department = course['department']
	number = course['number']
	name = course['name']
	db.session.add(Course(department=department, number=number, name=name))
db.session.commit()