# datathon
SFUSD Seat Allocation Datathon

Overview:
- This project aims to optimize the student program allocation within the San Francisco Unified School District (SFUSD) by creating a system that can split the Webster attendance area into two new areas for Webster Elementary and Mission Bay Elementary. The goal is to balance socioeconomic diversity, maximize student accommodation, and ensure contiguous zoning. The solution leverages various data sources and optimization techniques to produce a creative, functional, and impactful result.

Problem Statement:
- The San Francisco Unified School District (SFUSD) needs to optimize student program allocations for elementary schools. Specifically, the task is to split the Webster attendance area into two new attendance zones to serve students for both Webster and Mission Bay Elementary. The challenge lies in considering factors such as:
- Socioeconomic Diversity: Ensuring that the new boundaries prioritize socioeconomic diversity in each school.
- Maximizing Student Accommodation: Ensuring that all students in the Webster attendance area are placed in either Webster Elementary or Mission Bay Elementary without exceeding school capacity.
- Contiguous Zoning: Ensuring that the new zones are geographically contiguous and coherent.

Data Sources:
The project utilizes the following datasets:
- Student Application Requests: Information about students who applied to each school.
- Census Block Demographics: Demographic data on the population in the census blocks.
- School Seat Availability: The capacity of each school to accommodate students.

Approach:
1. Data Preprocessing:
- Clean and transform the provided datasets for efficient analysis and use.
- Integrate data on student applications, demographics, and seat availability.
2. Optimization:
- Use an optimization algorithm (e.g., linear programming, integer programming) to determine the most optimal split of the Webster attendance area into two zones.
- Focus on balancing diversity, maximizing seat usage, and maintaining contiguous zoning.
3. Evaluation:
- The solution will be evaluated based on creativity, complexity, presentation, functionality, and real-world impact.
- Consideration of real-world factors, such as school capacity and transportation routes, will be incorporated into the evaluation criteria.
4. Modeling and Algorithms:
- Use machine learning or optimization techniques to design and evaluate the zoning solution.
- Ensure that the model can scale to handle future changes in student population and school seat availability.

Technologies Used:
- Python: For data manipulation, optimization algorithms, and analysis.
- Pandas, NumPy: For data handling and analysis.
- Scikit-learn: For any machine learning algorithms if used in the model.
- Google OR-Tools: For optimization techniques.
- Matplotlib, Seaborn: For visualizations.
