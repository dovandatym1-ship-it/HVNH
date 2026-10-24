# Your First Process Vacation Request

- **Tài liệu nguồn:** `Your First Process - Vacation Request.pdf`
- **Định dạng gốc:** `.pdf`
- **Công cụ chuyển đổi:** MarkItDown (Microsoft Open Source)
- **Thời gian chuyển đổi:** 2026-10-13 19:48:23

---

First Workshop for Product
Evaluation
My First Process

Copyright © 2024 Bizagi

Table of contents

1.  Workshop: Vacation Request

Description of the Vacation Request Process

Scope

2.

Defining and modelling the Process

Studio

Process data

Forms creation

Activity: Register leave request

Activity: Verify available vacation days

Activity: Approve leave request

Activity: Register vacation leave

Activity: Inform reject reason

Business rules

Transition Conditions

Activity Actions

Performers

Activity: Register leave request

Activity: Approve leave request

Activity: Register vacation leave

Activity: Inform reject reason

Integrate with other applications

Invoke Web service from Bizagi

Work Portal

Users

4

4

4

6

6

17

29

30

36

36

39

42

43

43

47

54

55

55

57

58

60

60

65

65

Copyright © 2024 Bizagi

Parameters

Testing the Work Portal

Improving the work portal

Sending a notification (optional)

Conclusion

Next steps

Troubleshooting

FAQs

69

71

75

80

86

86

87

87

Copyright © 2024 Bizagi

1.  Workshop: Vacation Request

A  company  has  initiated  a  BPM  (Business  Process  Management)  strategy  and  has  chosen  Bizagi  to
support it. You have been selected to implement the Vacation Request Process.

The information about the Process and data to be controlled and visualized can be found in the
following pages. Follow step by step the instructions of this manual and you will have automated the
Vacation Request Process.

Description of the Vacation Request Process

The Vacation Request Process starts when an employee of the organization submits a vacation request.

Once the request is registered, it is received by the immediate supervisor; the supervisor must approve
or reject the request.

If  the  request  is  rejected  the  application  is  returned  to  the  applicant/employee  who  can  review  the
rejection reasons.

If the request is approved a notification is generated to the Human Resources representative, who must
complete the respective administrative procedures.

Scope

This Process focuses on controlling vacation requests of the organization, from the initial request up to
its approval or rejection.

Page 4 – My First Process

Copyright © 2024 Bizagi

Fig. 1. BPMN Vacation Request Process.

Page 5 – My First Process

Copyright © 2024 Bizagi

2.  Defining and modelling the Process

Studio

Process modelling is the foundational step in automating a process. In Bizagi Studio, the 'Model Process'
step  allows  you  to  visually  diagram,  model,  and document  business processes  using BPMN  (Business
Process Model and Notation), an industry-standard format for process modelling that is widely accepted
worldwide.

Open Bizagi Studio and click New process:

Fig 2. Creation of a New process in Bizagi Studio

The new process window will open, in the Process Name field type Vacation Leave Request.

Page 6 – My First Process

Copyright © 2024 Bizagi

 A Pool consisting of one Lane will load upon startup.  drag and drop 3 Lanes to the Process from the
Palette on the left side of the screen.

Fig 3.  Name process Vacation Leave Request

Fig. 4. Addition of Lanes to Pool.

Readjust the size of the Lanes so that you can see all the Lanes in your screen. To do this click on the
lines in between Lanes and move them up or down.

Page 7 – My First Process

Copyright © 2024 Bizagi

Fig. 5. Adjusting Lanes of Pool.

Rename the lanes with the following names: Employee, Supervisor and Human Resources Administrator. To
rename a Lane you need to right-click the Lane and select Edit Text. You can also double click on the text
of the Lane or click on the Lane and press F2.

Drag and drop a two Milestones from the Palette to add Phases.

Fig. 6. Renaming Lanes of Pool.

Page 8 – My First Process

Copyright © 2024 Bizagi

Fig. 7. Addition of Milestones to Process.

Rename the Phases; double-click the Milestone or click on the Milestone and press F2, change the name
of the first Phase to Register and the second to Approval.

Fig. 8. Edition of the name of the Milestones.

Now we will start to add shapes to our Process. Select the Start Event from the Palette and drop it at
the start of the Employee Lane.

Page 9 – My First Process

Copyright © 2024 Bizagi

Fig. 9. Addition of the Start Event.

The figures have a Pie Menu that allows Shapes to be easily included in the diagram. It is displayed when
you first put the Shape on the process or when you click on a Shape.

Fig. 10. Pie menu.

Select the Task Shape from the Pie Menu and place it next to the Start Shape.

Rename the new task to Register Leave Request. You can rename the Shapes when you first create them
or by double-clicking them.

Fig. 11. Task creation.

Page 10 – My First Process

Copyright © 2024 Bizagi

Important:

*All transitions must be properly connected, and all the Shapes must be inside Phases and Functional
Areas.

Add the remaining Shapes until the diagram looks like the following.

Right-click the Verify available vacation days Activity and transform it to a Service Task.

Fig. 12. Vacation Request Process.

Page 11 – My First Process

Copyright © 2024 Bizagi

Fig. 13. Task transformation to Service Task.

Now you need to configure three things:

•  Durations
•  Descriptions
•  Help texts

To do this right-click the Process name inside the diagram and select Properties.

Fig. 14. Selection of diagram Properties.

A column will appear on the right-hand side. Enter the following as the Description of the Process: “This
process controls the vacation requests of the employees of the company.”

Page 12 – My First Process

Copyright © 2024 Bizagi

Fig. 15. Edition of the Description of the diagram.

Located beside the Basic tab is the Runtime tab. Within this tab, you will specify the duration parameters
for the process. Provide values for the estimated duration, lower limit, and upper limit. These durations
are meant to comply with the Service Level Agreement (SLA) of your process. Note that the first dropdown
menu for the time parameters corresponds to hours, while the second dropdown menu corresponds to
minutes.

For this exercise, set the durations to 72 hours for the estimated time, 24 hours for the lower limit, and
96 hours for the upper limit. Once done, close the Properties window by clicking the "X" icon in the top
right corner.

Right-click Register Leave Request Activity and select Properties.

Fig. 16. Edition of the times of the Process.

Page 13 – My First Process

Copyright © 2024 Bizagi

Fig. 17. Edition of the Register Leave Request Activity.

The Element properties column will appear, switch to the Basic tab, and enter the following Description:
“This Activity allows the employee to enter the vacation request details.”

Fig. 18. Edition of the Register Leave Request description.

Switch to the Runtime tab and enter the following in the Help Text: “Include all the information in your
vacation request.”. The Help Text will be displayed to the end user when the Activity is executed in the
Work Portal.

In the same tab enter the time as shown below. Then, close the properties window of the Activity.

Page 14 – My First Process

Copyright © 2024 Bizagi

Fig. 19. Edition of the Help Text and Duration of the Register Leave Request Activity.

Configure the following properties for each User Activity:

Table 1. Properties of each User Activity.

Activity

Help Text

Approve leave request

Duration

48 hours

Inform reject reason

Review the reasons for request rejection.

72 hours

Register vacation leave

Post the event into the payroll system.

72 hours

Express the days in hours, for example: 2 days = 48 hours

Once you are finished, Save your changes and close the Process Modeler Suite.

When you close the Process Modeler, you will return to Bizagi Studio and be taken to the Process Wizard.
The Wizard guides you through all the necessary steps to automate your Process.

Page 15 – My First Process

Copyright © 2024 Bizagi

Fig. 20. Process Wizard.

Page 16 – My First Process

Copyright © 2024 Bizagi

Process data
Next,  we’ll  proceed  with  creating  the  data  model.  In  Bizagi,  the  data  model  encompasses  all  the
information required by the automated process for display in the Work Portal and for collecting inputs
from end users.

The Vacation Leave Request Process includes the following information:

•  Request date
•  Employee
•  Vacation start date
•  Vacation end date
•  Number of business days requested
•  Number of available days
•  Supervisor
•  Flag (yes/no) for approved vacations
•  Rejection reason
•  Payroll code
•  Administrative task date

All the information about the request such as dates, number of business days requested, and available
days will be grouped in the entity Vacation Request.

A standardized list about the possible rejection reasons will be designed in the entity Rejected Reason.

1.  Go to the second step of the Process Wizard and select Model Data:

Fig. 21. Process Wizard – Model data.

2.  A new window will appear. Enter the Process Entity, acts as the starting point and provides access to

the entire data model. Name it 'VacationLeaveRequest' and click OK.

Page 17 – My First Process

Copyright © 2024 Bizagi

Fig. 22. Process Entity declaration.

3.  A new window to design the data model, containing the Process Entity will appear. The creation of

entities, attributes, and relationships can be completed in this editor.

4.  Right-click the Vacation Request entity and select Edit Attribute List.

Fig. 23. Data model window.

Fig. 24. Edition attributes VacationLeaveRequest Entity.

Page 18 – My First Process

Copyright © 2024 Bizagi

5.  The Attribute List Window for the Vacation Request entity is displayed. Click the Add button to create

attributes. For each new attribute, complete the following information:

•  Display Name: This is name presented to the end user. It does not allow special characters.
•  Name:  This  field  will  be  automatically  filled  in  by  the  system  and  will  be  used  for  Business

Rules.

•  Type: This is the data type of the attribute.
•  Length: Applies for Strings; it determines the maximum length of characters the end user can

input in the field.

Create the following attributes:

Table 2. Attributes of VacationLeaveRequest Entity.

Display Name

Type

Length

Request date

Date - Time

None

Start date

Date - Time

None

End date

Date - Time

None

Business days requested

Integer

Available days

Integer

Approved?

Boolean

Rejection comments

String

Payroll code

String

None

None

None

100

20

Administrative task date

Date - Time

None

6.  The attribute list for the Vacation Request entity should resemble the illustration in the following

image. Note that you will need to click on 'Show advanced options' to adjust the length of a String.

Page 19 – My First Process

Copyright © 2024 Bizagi

Fig. 25. Addition of attributes in VacationLeaveRequest Entity.

7.  After you have created the basic attributes, proceed to create the attributes related to other

entities.

Page 20 – My First Process

Copyright © 2024 Bizagi

Fig. 26. Addition of Entity attribute in VacationLeaveRequest Entity.

Create the Rejection Reason Entity as a Parameter Entity, which requires its own attributes. To begin,
select  the  New  Entity  option.  A  new  window  will  appear,  allowing  you  to  create  the  Entity  and  its
attributes.

Our new entity will have the following information automatically:

•  Display Name: Name that will be displayed  in the form to the end  user; this field does not

allow special characters. It is going to be set to Rejection Reason.

•  Type: Parameter

Page 21 – My First Process

Copyright © 2024 Bizagi

Fig. 27. Entity Properties window.

The user must define if the entity’s values will be managed in the Production Environment by end
users, via the Work Portal. If not, the entity’s information will remain hidden for end users. In this case
Rejection  Reason  will  be  manageable  in  the  Production  Environment  because  its  values  do  not
determine the Process flow. They are just shown for informative reasons.

Click Next.

8.  The following window allows for the creation of attributes. This Entity will have one attribute, 'Rejection
Reason X', where the list of reasons to reject a request will be stored. (The reason for using 'Rejection
Reason X' instead of just 'Rejection Reason' is because an attribute cannot have the same name as
its parent Entity)

Table 3. Attributes of RejectionReason Entity.

Display Name

Type

Length

Rejection reason X

String

100

Page 22 – My First Process

Copyright © 2024 Bizagi

Fig. 28. RejectionReason Entity attribute creation.

Click Next.

9.  Enter a Display Attribute for the Entity. The Display Attribute is the visible attribute created for the
Entity that will be shown in the Work Portal when the Entity is referred to. Select the one you just
created.

Page 23 – My First Process

Copyright © 2024 Bizagi

Fig. 29. Declaration of the Display Attribute for the RejectionReason Entity.

Click Next.

10. A  Summary  window  appears.  Click  Finish  to  return  to  the  attribute

list  of  the  entity

VacationLeaveRequest.

Page 24 – My First Process

Copyright © 2024 Bizagi

Fig. 30. RejectionReason Entity summary.

The Entity VacationLeaveRequest is also related to a user Entity known in Bizagi as WFUser (Workflow
User). WFUser is created by default for all projects and is used to store all the information related to
end users. Since WFUser is already created by default, we just need to establish a relationship. Press
the 'Add' button and establish a relationship between 'Employee' and the SYSTEM entity. You can find
the WFUSER table under the 'Entity' option and then the 'System' sub-option." Click Next.

Page 25 – My First Process

Copyright © 2024 Bizagi

Fig. 31. Addition of Employee as a WFUser System Entity Type.

11. Click Next. A Summary window pops-up for the VacationLeaveRequest entity.

Page 26 – My First Process

Copyright © 2024 Bizagi

Fig. 32. VacationLeaveRequest Entity summary.

12. Click Finish. The data model is now complete and presented graphically. You may need to reposition

the entities on the screen by dragging them to the desired position.

13. Select the option Add Related Entities by right clicking the VacationLeaveRequest Entity.

Fig. 33. Vacation Leave Request Process Data Model.

Page 27 – My First Process

Copyright © 2024 Bizagi

14. The complete diagram is displayed. Save and close the window.

Fig. 34. Add Related Entities Button.

Fig. 35. Complete Vacation Leave Request Process Data Model.

Page 28 – My First Process

Copyright © 2024 Bizagi

Forms creation
Once the Process Diagram and the Data Model are ready, we will proceed to create the forms associated
with  each  one  of  the  human  activities  of  the  Process.  Forms  are  used  to  enter,  and  display  required
information, so that end users can interact with the Process.

Fig. 36. Process Wizard define Forms step.

Bizagi  empowers  modern  businesses  to  embrace  the  mobile  work  revolution  and  elevate  business
process automation to new heights. With our powerful Forms designer, you can create a unique user
interface tailored to your needs. Bizagi automatically optimizes the display of information for each specific
device, ensuring an optimal user experience across all platforms.

Move to the next step of the process and click on Define Forms.

Page 29 – My First Process

Copyright © 2024 Bizagi

Fig. 37. Bizagi in different platforms.

Activity: Register leave request
The first Activity of the Process, Register Leave Request will have a warning label on the top right corner.
Click on this Task.

Fig. 38. Selection of the Register Leave Request in the Forms view.

This is the information that this Task must contain:

Fig. 39. Register Leave Request goal form.

We will guide you on how to create this form.

1.  Upon clicking on the Register Leave Request activity, the following screen will appear:

Page 30 – My First Process

Copyright © 2024 Bizagi

2.  Click the Controls tab and subsequently click on the Container label. Drag and drop a Group to the

DROP HERE section.

Fig. 40. Form creation window.

3.  Double-click it and type Request information.

Fig. 41. Dragging of a Group to a Form.

Page 31 – My First Process

Copyright © 2024 Bizagi

Fig. 42. Renaming Group in Form to ‘Request information’.

4.  Go to the Layout tab to include a layout. Layouts help distribute the information and make it more

appealing.

Drag and drop a 50%-50% layout into the DROP HERE section within the Group.

Fig. 43. Aggregation of a Layout into a Group.

5.  Click the Data tab to include the attributes in the layouts. Drag and drop the elements we want as per

Fig. 42 from the Data Model.

Page 32 – My First Process

Copyright © 2024 Bizagi

6.  Request date: Drag and drop the attribute in the first quadrant of the layout.

Fig. 44. Aggregation of Request date into the Layout.

This field must be read only. Click the field, on the left-hand side you will see the Basic Properties of
Request  date  Properties.  Locate  the  Editable  property  and  select  the  No  option  (Cross  icon).  This
makes the control read only.

Fig. 45. Changing editability of a field.

7.  Employee: Drag and drop the attribute in the second quadrant of the layout. This field must be read
only. Set this control as non-editable by opening the Editable property and select the cross mark. This
makes the control read only.

Page 33 – My First Process

Copyright © 2024 Bizagi

Fig. 46. Aggregation of Employee into the Layout and change of editability.

8.  The Employee attribute is related to the WFUSER system entity. Therefore, it is necessary to relate a

Display Attribute. Locate the Display attribute property and select Full Name.

Fig. 47. Aggregation of the ‘Employee’ attribute into the Layout and edition of display attribute.

9.  Go back to the Data tab. Drag and drop the following attributes from the Data Model as shown below.

Start date – End Date – Business days requested.

Page 34 – My First Process

Copyright © 2024 Bizagi

Fig. 48. Aggregation of other attributes to the form.

10. These  fields  will  be  mandatory.  Select  them  all  holding  down  the  CTRL  key.  Their  Properties  are

displayed. Select the Check mark on the Required property.

11. Save the form and close it to return to the Process Wizard.

Fig. 49. Edition of fields to mandatory.

Page 35 – My First Process

Copyright © 2024 Bizagi

Activity: Verify available vacation days
Since  this  is  an  automatic  Task,  no  Form  must  be  related.  In  step  6  of  the  Process  Wizard  (Define
Integration Interfaces) we will see how the configuration is done for this Task.

Activity: Approve leave request
1.  Select the Activity Approve leave request.

The Forms Designer will open.

The first part of the Form will be the same as the one designed before, so we will use the Copy From
option to help us design faster.

Fig. 50. Creation of a Form in Approve leave request.

Fig. 51. Copy from button in the form editor

A new window displaying the Process flow opens. Select the Register leave request Activity by clicking it.
Click OK.

Page 36 – My First Process

Copyright © 2024 Bizagi

Fig. 52. Copying of a Form from another Task.

2.  The information is copied exactly as in the original form. To make the Controls Start date, End date and

Business days requested read only we should set the Editable properties to False. Select them all at the

same time clicking them while holding down the CRTL key and select not editable in the properties.

Fig. 53. Changing editability of Start date, End date and Business days requested.

3.  Add  a  new  Group  under  the  existing  one.  Go  to  the  Controls  tab,  then  drag  and  drop  a  Group

underneath the existing one. Change its name to Approval information.

Page 37 – My First Process

Copyright © 2024 Bizagi

4.  The following controls will be entered, without a Layout.

Fig. 54. Addition of another Group to the From.

•  Available days: Must have the Editable property set to ‘No’.
•  Approved: The Required property should be set to ‘Yes’ since this field is mandatory.
•  Reject reason
•  Rejection comments
•  Employee´s Supervisor: Locate the Employee attribute in the data model. Expand it and
drag and drop Employee – Boss user id – Full Name attribute to the form. This control
must  be  read  only.  Change  the  display  name  by  double-clicking  the  field  and  type:
Employee’s Supervisor.

Fig. 55. Addition of the Employee’s Supervisor attribute to the Form.

5.  Click the Save button once the Form has been completed and close it.

Page 38 – My First Process

Copyright © 2024 Bizagi

Activity: Register vacation leave
The creation of the form Register vacation leave will contain the information of the Supervisor’s Form as
read-only and include the Controls that the Human Resources Assistant must complete.

1.  Select the Activity Register vacation leave on the third step of the Process Wizard.

We  will  add  all  the  information  we  included  on  the  Register  leave  request  and  Approve  leave  request
Activities, as read only as we did in the previous step. Go to the Copy from option and select Approve
leave request Task. Click OK.

Fig. 56. Copying the Form Approve leave request for Register vacation leave.

2.  Change the Editable property to not editable for all Controls, in their respective Properties.

Page 39 – My First Process

Copyright © 2024 Bizagi

Fig. 57. Changing the editability Property of the Controls.

3.  Include a Group on the bottom of the Form, by dragging and dropping a Group (found in the Controls

tab). Change its name to Register leave request.

Then, include a 50%-50% Layout in the group, by going to the Layout tab and dragging and dropping
the layout in the new group.

Page 40 – My First Process

Copyright © 2024 Bizagi

Fig. 58. Addition of a 50%-50% Layout inside the new Group.

4.  Go back to the Data tab. Drag and drop the attributes Administrative task date and Payroll code to each

side of the new layout. Make them both mandatory (Required Property).

5.  Click the Save button and close the Form.

Fig. 59. Edition of the Required Property of the Controls.

Page 41 – My First Process

Copyright © 2024 Bizagi

Activity: Inform reject reason
Click the Activity Inform Reject Reason, in the third step of the Process Wizard. Once again, use the Copy
from option and copy the information from the Approve leave request Activity.

Set the Editable property to No for all the fields.

Fig. 60. Edition of the Editable Property of the Controls.

Click the Save button and close the Form. Click at the top right corner of the Forms Designer to return
to the Process Wizard view.

Page 42 – My First Process

Copyright © 2024 Bizagi

Business rules
The next step in the Process Wizard is the definition of business rules that control the Process routing.

The first rules to be completed are known as transition rules. These rules evaluate conditions and decide
where the Process flow is to continue. They return True or False and they are associated to Gateway
shapes.

We will create rules for the Leave request approved? Gateway: If the request was approved, the Process
flow will continue to the Register vacation leave Task. If not, it will continue to the Inform reject reason Task.

Since there are two paths after the Gateway, we will create a rule for one of the Transitions and make the
other the default Else condition.

Transition Conditions
1.  To create a Business Rule, go to the fourth step of the Process Wizard and select Define Expressions:

Fig. 61. Selection of the Define expression button in the 4th step of the Wizard, Business Rules.

2.  The Rule editor will open highlighting the transitions that have no rule associated with them:

Page 43 – My First Process

Copyright © 2024 Bizagi

3.  Select the transition named Yes that reaches the Activity Register vacation leave by clicking the transition.

Fig. 62. Define Expressions diagram.

Three options are presented:

•  Always: when selected Bizagi will always take that path ignoring the other sequence flows.

•  Else:  when  selected  Bizagi  will  take  that  path  when  no  other  path  is  valid.  We  recommend

always having one sequence flow with this option.

•  Based on the result of an expression: when selected Bizagi will evaluate an expression to take

or not the selected path.

4.  Select  Based  on  the  result  of  an  expression.  The  list  of  system  Expressions  and  previously  created

Expressions opens. Since there are no expressions created, click New.

Page 44 – My First Process

Copyright © 2024 Bizagi

Fig. 63. Based on the result of an expression.

5.  The Boolean Expression editor opens.

Fig. 64. Creation of a new Expression.

Drag and drop the attribute Approved from the Data Model at the left to the condition item. Select
the function is Equal to and choose the true option:

Page 45 – My First Process

Copyright © 2024 Bizagi

6.  Click OK.

Fig. 65. Construction of a new Expression.

7.  Select the transition from the gateway that reaches the Inform Reject Reason Task by clicking it.

Select Else from the options displayed, and then click OK.

8.  Go back to the Process Wizard by clicking at the top right corner of the screen.

Fig. 66. Selection of the Else option for the other route.

Note: In exclusive gateways Bizagi will give priority to the sequence flows with expressions over the ones
with Always selected. That is, in a single exclusive gateway, if a sequence flow has Always defined and

Page 46 – My First Process

Copyright © 2024 Bizagi

another sequence flow has an expression, Bizagi will take the expression path and disregard the Always
path, when the expression is met.

Activity Actions
We will create rules to automatically fill-in the fields Request date and Employee; this way, when a case is
started  these  two  Controls  will  be  filled  by  Bizagi  containing  the  information  of  today’s  date  and  the
Employee logged in.

These rules will be created in the first Activity of the Process; we will include an Expression that sets the
Date of the Request and to save the Case Creator as the Employee.

1.  Go to the fourth step of the Process Wizard and select Activities Actions.

Fig. 67. Selection of the Activity actions button in the 4th step of the Wizard, Business Rules.

2.  A new window opens, in this window you will see the different Tasks, you can add actions to these

Activities. Select the Register leave request Activity.

3.  Select the On Enter option. Then click the Plus icon to add an Action and select Expression.

Page 47 – My First Process

Copyright © 2024 Bizagi

Fig. 68. Activity actions On Enter Expression creation.

4.  The list of previously created expressions opens. Click New.
5.  The Expression editor opens. Fill the Display Name and Description as follows; this information will let

you identify the Expression for later use.

6.  Right-click the arrow and select Add Expression. Type Applicant and Date and click OK.

Fig. 69. Creation of new Expression.

Page 48 – My First Process

Copyright © 2024 Bizagi

7.  Right-click the module just included and select Properties.

Fig. 70. Creation of new Expression.

8.  The  Expression  editor  opens.  Click  Data  Model  and  select

the  Employee  attribute.

Fig. 71. Selection of Properties of the new Expression.

Click OK.

Page 49 – My First Process

Copyright © 2024 Bizagi

Fig. 72. Edition of Expression.

Fig. 73. Selection of the Employee attribute.

9.  The Employee attribute has been added to the Expression. Now enter an equal sign and then select

the Function option.

Navigate to the Case creator user Category, and then select the User Id of the case creator function.

Page 50 – My First Process

Copyright © 2024 Bizagi

Click OK. Add a semicolon to demarcate the statement.

10.

The first assignment is finished; the Employee user will be the case creator.

Fig. 74. Selection of the Employee attribute.

We will now set the Request date as the creation date. Position your cursor on the next line and open
the data model. Select the Data Model option and then select the Request date attribute. Click OK.

Fig. 75. Selection of the Request date attribute.

Page 51 – My First Process

Copyright © 2024 Bizagi

11.

The Request date attribute has been added to the Expression. Now enter an equal sign and then

select the Function option.

Navigate to the Date & time Category, and then select the Today function. Click OK.

Fig. 76. Selection of the Request date attribute.

Note: The difference between Today and Now is that Today returns only today’s date, Now on the other
hand returns today’s date and the exact time (hour, minute, second).

12.

Click the OK buttons to save the assignments, save the rule and close the Activity Actions editor.

Page 52 – My First Process

Copyright © 2024 Bizagi

Fig. 77. Expressions of Employee and Request date.

13.

Return  to  the  Process Wizard  by  clicking on  Home  in the drop-down menu  in  the  upper  right

corner of the diagram space.

Page 53 – My First Process

Copyright © 2024 Bizagi

Performers
The Performers assignment is a very important stage within Bizagi.  The responsible resources for each
one of the Process activities are defined in this stage.

Bizagi identifies the relationship that exists between the different employees based on the variables that
characterize  and  differentiate  them.  Thanks  to  this  functionality,  Bizagi  has  the  capacity  to  allocate
Activities to the different company members.

First, we must define what would be an appropriate assignment for each one of the Process activities;
later, the configuration will be completed in Bizagi:

•  The access to the Vacation Leave Request Process is an internal process that must be available

for all the employees of the organization. Thus, the first Activity must always be available for

anyone who creates the case.

•  The employee’s supervisor will ALWAYS complete the Activity Approve leave request.

•  The user who submitted or created the request will ALWAYS complete the Activity Inform Reject

Reason. (The reason for rejection is completed by the supervisor but ALLOCATED to the

requester).

•  The Inform Reject Reason Activity should ALWAYS be allocated to the person who submitted or

created the case.

•  The Human Resources Assistant will ALWAYS be responsible for the Register vacation leave

Activity.

To configure the named allocations, go to the fifth step of the Process Wizard.

The activities that do not have a Performer configured are highlighted in the workflow.

Fig. 78. Performers step in the Process Wizard.

Page 54 – My First Process

Copyright © 2024 Bizagi

Fig. 79. Workflow diagram where missing Performer configuration is highlighted.

Activity: Register leave request
This Activity must be assigned to the creator of the case; this is a default functionality Bizagi provides, so
we don’t have to create an assignment for it.

Activity: Approve leave request
1.  Select the Activity by clicking it, the Performers assignment window will appear.

2.  Click Add condition (this is the red plus sign at the edge of the blue And circle).

Fig. 80. Performer assignment window.

Page 55 – My First Process

Copyright © 2024 Bizagi

Note: The different circles at the edge of the main circle correspond to different things: The little

blue  plus  circle  corresponds  to  the  addition  of  an  And.  The  purple  plus  circle  corresponds  to  the

addition of an Or. Finally the red plus circle corresponds to the addition of the condition related to

that And or Or. See Fig. 77.

Remember that the main circle can also be an Or. See Fig 78.

Fig. 81. And condition with its associated conditions.

Fig. 82. Or condition with its associated conditions.

3.  In the new window we will select the Supervisor as the performer. Select User Id and then in the Value

section press the plus button on the right side next to the word expression.

4.  The list of system expressions is displayed.

Fig. 83. Performer Expression creation.

Page 56 – My First Process

Copyright © 2024 Bizagi

Fig. 84. Selection of CurrentAssigneeBoss value in the Expression manager.

5.  Select  the  CurrentAssigneeBoss  and  click  OK.  This  instruction  automatically  assigns  the  creator’s

Supervisor to the second task.

The Expression must look like this:

6.  Click OK to save the Performer Condition and OK again to save the performer.

Fig. 85. Final Expression.

Activity: Register vacation leave
1.  Repeat steps 1 and 2 of the Approve leave request Activity but for the Register vacation leave Activity. This

task is performed by an employee in the Human Resource department holding a position of Human

Resource Assistant.

Page 57 – My First Process

Copyright © 2024 Bizagi

2.  Since we have no Positions created, we will create one:

Fig. 86. Expression creation using the Position Property.

In  the  first  drop-down  list,  select  Position.  A  new  drop-down  list  is  enabled  at  the  right.  Select
Organization. This enables the New link.

Fig. 87. Expression creation adding a new Value.

3.  Type Human Resources Assistant and click on the green tick, finally click on the Ok button to save the

Assignment.

Fig. 88. Expression creation adding a new Value.

Activity: Inform reject reason
The Inform Reject Reason Activity should ALWAYS be allocated to the person who created the case.

1.  Repeat steps from 1 to 4 of the Approve leave request Activity but for the Inform reject reason Activity.

2.  Select the Case Creator of the case and click OK to save the condition.

Page 58 – My First Process

Copyright © 2024 Bizagi

Fig. 89. Selection of Case creator in the Expression manager window.

3.  Save the rule by clicking OK for the Performers window.

Close the Diagram by clicking the
return to the Process Wizard.

 button located at the top right corner of the screen to

Page 59 – My First Process

Copyright © 2024 Bizagi

Integrate with other applications

Web Services will be used to integrate the Bizagi Process with the payroll system. It exposes a service
that returns the number of available vacation days for a specific employee.

Invoke Web service from Bizagi
1.  From the Project Wizard go to the sixth step and select Define Integration Interfaces.

Fig. 90. Selection of the Define integration interfaces button in the 6th step of the Process Wizard.

2.  A view of the Process is presented. In this view, only the service Tasks are going to be active. Click the

task Verify Available Vacation Days.

Page 60 – My First Process

Copyright © 2024 Bizagi

Fig. 91. Process seen in the Define Integration Interfaces stage.

3.  The Interface Wizard opens. Type the URL.

https://legacy.bizagi.com/ESB/ESBServices.asmx

a.  Click  Go  to  see  the  available  methods  (this  operation  could  take  some  time  to  finish).

Select  the  method  verifyAvailableVacationDays  and  click  Next  (the  System  and  Interface

Name take default values that can be change if desired).

Page 61 – My First Process

Copyright © 2024 Bizagi

4.  In this step the information from Bizagi to the web service will be configured. Two tables are shown,

on the left is Bizagi’s data model and on the right the information the web service method expects.

Fig. 92. Integration Wizard.

Fig. 93. Web Service Connector.

Since the Employee’s (Applicant) username is used to obtain the available Vacation Days, in the Bizagi
Data table, expand the VacationLeaveRequest element and go through the entities tree until you see the
Employee’s username.

Once  the  desired  attribute  is  reached,  click  the  userName  attribute,  and  then  click  the  UserName
parameter at the right this automatically connects the two items.

Page 62 – My First Process

Copyright © 2024 Bizagi

Fig. 94. Connection of the userName of the Database with the userName of the Web Service.

The tables can be moved and re-sized if needed; also, the window can be maximized using the
at the upper right corner.
If the window is maximized, restore it to see the taskbar again and click Next to continue.

button

5.  In the next window select we need to select where in Bizagi’s data model, the web service response is

going to be saved. As in the previous step, two tables are shown but now the table with the web service

response is on the left and the one with Bizagi Data on the right.

Fig. 95. Output data connection diagram.

Page 63 – My First Process

Copyright © 2024 Bizagi

In Bizagi Data, under VacationLeaveRequest find the attribute Availabledays and match the response from
the web service to this attribute. Then Click Next.

Fig. 96. Connection of result of the Web Service with the Database.

6.  On the final step we will configure what to do if an error occurs, select the option Throw Exception from

the Action list, and click Finish.

7.  The Interface wizard will close. Return to the Process Wizard.

Fig. 97. Selection of Exception Action.

Page 64 – My First Process

Copyright © 2024 Bizagi

Work Portal
So far, the Process flow chart has been completed along with the structuring of the Process information,
the  Forms  design  for  each  one  of  the  Process  activities,  the  definition  of  the  business  rules  and  the
Performers.  Now we are ready to configure the Work Portal.

Click the seventh step of the Process Wizard. In the new window select Run.

You can also click the green icon in the Ribbon for a quick access to the Portal.

Fig. 98. 7th step of the Process Wizard.

Fig. 99. Work Portal button.

Users
The work portal will need to have three users so that the behaviour of the assignments can be verified.
We will now create the three users directly from the web application. The following table presents the
users list.

Page 65 – My First Process

Copyright © 2024 Bizagi

Table 4. Work Portal users.

User

Password

Domain

Supervisor

Supervisor

Employee

Employee

Assistant

Assistant

domain

domain

domain

Job Title

Immediate
Supervisor

Supervisor

Human Resources
Assistant

Supervisor

1.  To create the user, select the Admin Menu and click the Users option.

2.  Click New User.

Fig. 100. Work Portal User creation.

3.  Fill out the information from the user list table presented at the start of this section.

Fig. 101. Work Portal User creation.

Page 66 – My First Process

Copyright © 2024 Bizagi

Fig. 102. User creation.

BE CAREFUL to include a password you can remember or use the one in the given table. Bizagi will assign
the User Name as password by default.

Deselect all checkboxes in the Basic Information tab: Expired Password, Locked Account and Send Mail with
Password to User. Doing so bypasses authentication and SMTP server validations.

4.  Go to the next tab and select the Organization from the list of Organizations by clicking >>”.

Fig. 103. Supervisor creation.

Fig. 104. Organization declaration.

5.  Click Save to Save the Supervisor user.

Employee (Applicant)

1.  Repeat steps 1 to 4 from the Supervisor user creation.

Page 67 – My First Process

Copyright © 2024 Bizagi

2.  To fill in the Supervisor field for the Employee user go to the Configuration User Tab and click the Search

icon (

).

3.  Click Select in the Supervisor record.

Fig. 105. User configuration.

Fig. 106. User selection.

4.  Click Save to save the Employee user.

Assistant

1.  Repeat steps 1 to 3 from the Supervisor creation.

Page 68 – My First Process

Copyright © 2024 Bizagi

2.  To Add the Position for the Assistant user, go to the Organizations tab. Select the Organization from

the list of Organizations by clicking >>”.

3.  The Organization group is displayed. Select the position you want to add and click “>>” to add it. Save

the user by clicking Save.

Fig. 107. Organization declaration.

Fig. 108. Organization declaration.

Parameters
Before executing the Process, we must define rejection reasons.

1.  Go to the Model data option in the Process Wizard, right click the Rejection Reason entity and click

Values.

Page 69 – My First Process

Copyright © 2024 Bizagi

2.  Click the Reject Reason button at the bottom of the new window.

Fig. 109. Model data stage in the Process Wizard.

3.  Enter the possible rejection reasons:

Fig. 110. Creation of rejection reasons.

Table 4. Rejection Reasons.

Reject Reasons

Commitments make it impossible to take vacations on that date.

No replacement available.

Important event on the requested date.

No available days.

Other reason.

Page 70 – My First Process

Copyright © 2024 Bizagi

4.  Save the model and click Close.

Fig. 111. Rejection reasons.

Testing the Work Portal
We will verify the Process after the information for the Parameter entities and users has been entered.

Open the Work Portal.

You’ll  be  asked  to  enter  one  of  the  credentials  for  the  users  created.  Enter  the  application  using  the
Employee User:

Fig. 112. Bizagi login screen.

NOTE: If you have problems logging into the Work Portal check our Trouble shooting section, items 3 and
4.

1.  Click the New option and select the name of the Process: Vacation Leave Request.

Page 71 – My First Process

Copyright © 2024 Bizagi

2.  Complete the information for the Activity; click Next to continue with the Process. You are informed

that you have no pending activities for the Process. The assignee is now the Supervisor.

Fig. 113. Case creation.

3.  Log out from the application and Log in again with the Supervisor user.

Fig. 114. Case creation.

Page 72 – My First Process

Copyright © 2024 Bizagi

Fig. 115. Supervisor login.

Fig. 116. Case created.

The case is displayed in the Supervisor’s Inbox as a pending task. Click Work on it to enter the case.

4.  Fill in the information of the Activity; approve the request and click Next.

Fig. 117. Vacation Leave Request Case.

Page 73 – My First Process

Copyright © 2024 Bizagi

5.  Log in again with the Assistant user.

Fig. 118. Vacation Leave Request Case.

The Register vacation Leave Activity is shown.

Fig. 119. Assistant login.

Page 74 – My First Process

Copyright © 2024 Bizagi

If  the  request  was  not  approved,  then  the  Inform  Request  Rejection  screen  will  be  displayed  to  the
Employee user.

Fig. 120. Vacation Leave Request Case.

Fig. 121. Vacation Leave Request Case.

Improving the work portal
Bizagi allows the modification of the controls’ appearance within the forms to achieve the look you desire.

Bizagi also  offers  a  set of  tools, that allow  validating  the  information entered  to  ensure  that  the  data
entered by end users is adequate for each Activity and fulfils the different business conditions.

For this workshop we will show how to improve the user interface.

The Rejected Reason in the Approve leave request Activity should be displayed to the user only when the
request  is  rejected;  some  Actions  will  be  implemented  in  the  Forms  Designer  to  implement  that
functionality.

1.  Go to the third step of the Process Wizard and open the form associated to the Approve leave request

Activity.

2.  Open the Actions & Validations option and click the Add button on the window displayed.

Page 75 – My First Process

Copyright © 2024 Bizagi

Fig. 122. Actions and Validations.

3.  Select the If condition. Click Add a condition.

4.  Scroll to the Control Approved. Then, choose the Operator Is False.

Fig. 123. Add a condition.

Page 76 – My First Process

Copyright © 2024 Bizagi

5.  Go to the Then section. Click Add an Action.

Fig. 124. Action editor.

Select the Command Set required for, the Control Reject Reason and the Argument Yes. This way when
the Approved Control is false, the Reject Reason will be required.

Repeat the procedure for the field Rejection Comments.

6.  Add two more Actions: Select the Command  Change visibility for, the Control Reject Reason and the

Argument Yes. This way when the Approved Control is false, the Reject Reason will be visible.

Fig. 125. Add an Action.

Repeat the procedure for the field Rejection Comments.

Page 77 – My First Process

Copyright © 2024 Bizagi

7.  Click the Else button.

Fig. 126. Action addition.

Fig. 127. Action editor.

8.  Select the Command Change visibility for, the Control Reject Reason and the Argument No. This way

when the Approved Control is Yes or not filled, the Reject Reason will be hidden.

Repeat the procedure for the field Rejection Comments.

Do the same for  the Set required for command  to avoid  mandatory fields when they are no longer
necessary. After pressing OK you need to close the windows by pressing X.

Page 78 – My First Process

Copyright © 2024 Bizagi

Fig. 128. Action addition.

9.  The  new  Action  for  RejectedReason  and  RejectionComments  can  be  observed  by  going  to  the

Approve Vacation Request Task in the Work Portal and selecting  Yes or No for the Field Approved.

Click OK.

Fig. 129. New Action.

Page 79 – My First Process

Copyright © 2024 Bizagi

Fig. 130. Final Request.

Sending a notification (optional)
The Process could be changed to send an automatic notification for the Inform Reject Reason Activity, to
do this  the  Activity  needs  to be  converted  into  a  service  task.  A  SMTP  (Simple  Mail  Transfer  Protocol)
Server is preconfigured in Bizagi PaaS.

1.  Go to the first step of the Process Wizard and open the Process.

2.  Right click the Inform Reject Reason Activity and select Script Task under the Task type options:

Fig. 131. Script Task selection.

3.  Save the Process and close the Modeler. Go to the fourth step of the Process Wizard and select the

option Activity Actions.

4.  Click the Inform Reject Reason Task and Add an On Exit – e-Mail.

Page 80 – My First Process

Copyright © 2024 Bizagi

5.  On the Message Window fill the To field as follow VacationLeaveRequest-Employee-ContactEmail

Fig. 132. Mail selection.

6.  Include a subject as: Your Vacation Request has been Rejected

Fig. 133. Email attribute selection.

7.  A text like this one must be included in the message:

Dear (Applicant full name):

We are sorry to inform you your Vacation Request has been rejected. The reason for this rejection as
follow:

(Reject Reason)

To include the applicant’s full name and Reject Reason, select the XPath Field option.

Navigate in the Data Model and select the attribute. Click OK. The attribute is now included.

Page 81 – My First Process

Copyright © 2024 Bizagi

Your e-mail should look like this:

Fig. 134. Full name attribute.

Fig. 135. Mail configuration.

8.  Click Apply and Save to close the e-mail Definition Window and then OK in the Activity Actions

Window.

9.  Configure the Contact e-mails for the Employee. Go to the Work Portal, Admin-Users:

Page 82 – My First Process

Copyright © 2024 Bizagi

Make sure the e-mail is a valid e-mail address and click Save.

Fig. 136. User creation.

10.

 Run the Application. Start a new case and reject the request, instead of looking to a form for the

Inform Reject Reason Activity an e-mail will be sent, and the case will be closed. The e-mail would have

to look like this:

Page 83 – My First Process

Copyright © 2024 Bizagi

Fig. 137. Email test.

Ensure that the Enable Email checkbox is selected for this test to function properly.

To verify that the Enable Email checkbox is selected, follow these steps:

1.  In the Bizagi Studio window, click on Cloud Services in the top menu bar.

2.  Select the Management Console Web button.

3.  Once the Management Console page opens, navigate to the Environment section.

4.  Under the Options section, ensure the Enable Email checkbox is selected.

Page 84 – My First Process

Copyright © 2024 Bizagi

Fig. 138. Management Console button in Studio.

Fig. 139. Enable Email Checkbox.

Page 85 – My First Process

Copyright © 2024 Bizagi

Conclusion
In  this  workshop  you  learned  to  diagram  the  flow  of  Processes,  the  design  and  creation  of  its  data
structure,  the  definition  of  business  rules,  and  configuration  of  assignment  rules  for  each  one  of  the
manual Activities and to connect with other applications via web.  The result was an easy-to-use Work
Portal, which shows accurately the model created in Bizagi Studio; this result could be achieved because
of the data driven concept of Bizagi.

Thank you for completing this workshop, for Bizagi it has been a pleasure to show you why we are the
most agile solution to automate Process.

We hope that your experience with Bizagi has been satisfactory; If you have any questions or comments,
Feel free to Contact us.

If you need to review the solution of the workshop, you can open Bizagi and the project will be available.

Next steps

1.  Check our documentation at https://help.bizagi.com/platform/en

2.  Do the Second Workshop for Product Evaluation to learn more advanced features.

Page 86 – My First Process

Copyright © 2024 Bizagi

Troubleshooting

FAQs

This section deals with the most frequent questions arising from this workshop exercise:

1.  I added the wrong shape.  How do I delete it?

Select the shape and press the delete key. A Lane can be deleted simply by right-clicking the name
and selecting the Delete option. Before deleting the lane, there should be no shapes associated with
it. To delete a Phase, select the Delete option that appears when you right-click the top of the Phase.
Remember that to be able to delete a Phase, there should be no associated shapes to the left of said
phase.

2.   I forgot to uncheck the checkboxes when I added the user.

When logging into the Work Portal, you will be asked to change your password.  This may result in an
authentication error. Refer to question 4 to resolve the matter.

3.   I can’t log in with the user I created. I get an authentication error.

For this workshop, you need to bypass the authentication validation.  In the Welcome page, select the
Administrator Login at the bottom right. In the new window, leave the Password blank and click Login.
The Work Portal will run with Bizagi’s default-created user: admon.

To edit the user, select Admin-Users and deselect all checkboxes in the Basic Information tab: Expired
Password, Locked Account and Send Mail with Password to User.  Check the Password field is filled. Doing
so will bypass authentication and SMTP server validations.

4.  I still can´t login, users are all blocked.

Open  Bizagi  Studio  and  click  the  Expert  icon  located  at  the  upper  left  corner.  This  will  enable  the
Modules view, which is an advanced view. Go to Security module and locate Enable Quick Login as
shown in the image below.

Page 87 – My First Process

Copyright © 2024 Bizagi

Click Update.

Fig. 140. Expert view.

When Quick Login is enabled you will not have to enter the user’s password in the Work Portal, just
select the user you want to log in with. Click Run to test the Work Portal.

5.  I do not see the expected Activity when logging into the Work Portal.

Ensure you have assigned the correct Performer to each one of the Process activities. Take care to
login with the appropriate user.

Page 88 – My First Process

Copyright © 2024 Bizagi

