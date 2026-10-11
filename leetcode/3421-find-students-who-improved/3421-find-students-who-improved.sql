# Write your MySQL query statement below
# Write your MySQL query statement below

select * from (
select student_id,subject,
max( case when asc_rnk = 1 then score end) as first_score,
max( case when desc_rnk = 1 then score end) as latest_score
from (
select student_id,subject,score,exam_date,
row_number() over( partition by student_id,subject order by exam_date) as asc_rnk,
row_number() over( partition by student_id,subject order by exam_date DESC) as desc_rnk
from scores
) t1
group by student_id,subject
having count(distinct exam_date) > 1
) t2
where latest_score > first_score
order by student_id, subject