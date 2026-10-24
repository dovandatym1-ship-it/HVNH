# Final Project LoanAssessment K28

- **Tài liệu nguồn:** `Final Project - LoanAssessment K28.pdf`
- **Định dạng gốc:** `.pdf`
- **Công cụ chuyển đổi:** MarkItDown (Microsoft Open Source)
- **Thời gian chuyển đổi:** 2026-10-13 19:48:42

---

KHOÁ CAO HỌC K28 NGÀNH HỆ THỐNG THÔNG TIN QUẢN LÝ

BÀI TẬP LỚN CUỐI KHOÁ

Loan Assessment Process

Business Process Management

www.bizagi.co m

Hanoi, 10/2026

Table of Contents

INTRODUCTION TO BIZAGI BPM SUITE ........................................................................................................................... 3

WORKSHOP: LOAN ASSESSMENT PROCESS................................................................................................................. 4

DESCRIPTION OF THE LOAN ASSESSMENT PROCESS ............................................................................................................. 5
SCOPE ............................................................................................................................................................................................... 5
ACTIVITY: CHECK APPLICATION FORM.................................................................................................................................... 30
ACTIVITY: CHECK CREDIT HISTORY .......................................................................................................................................... 35

ACTIVITY: APPRAISE PROPERTY ................................................................................................................................................ 41
ACTIVITY: ASSESS ELIGIBILITY ................................................................................................................................................... 42
ACTIVITY: PREPARE AND SEND ACCEPTANCE PACK ............................................................................................................. 46
ACTIVITY: PREPARE AND SEND INSURANCE QUOTE ............................................................................................................ 51
ACTIVITY: VERIFY PAYMENT AGREEMENT............................................................................................................................... 55
ACTIVITY: TAKE FINAL DECISION .............................................................................................................................................. 56
PROCESS ROUTING...................................................................................................................................................................... 62
Gateway 1. Form complete?............................................................................................................................................ 63
Gateway 2. Applicant eligible? ....................................................................................................................................... 65
Gateway 3. Quote requested?........................................................................................................................................ 66
ACTIVITY EVENTS ......................................................................................................................................................................... 66
Set Loan Officer and Revision date ............................................................................................................................. 67
Set Loan Officer, Financial Officer, Property appraiser and Sales representative.............................. 71
Set Status................................................................................................................................................................................... 72
Set the Risk Weight.............................................................................................................................................................. 74
ACTIVITY: CHECK APPLICATION FORM.................................................................................................................................... 80
ACTIVITY: CHECK CREDIT HISTORY .......................................................................................................................................... 81
ACTIVITY: APPRAISE PROPERTY ................................................................................................................................................ 82

ACTIVITY: ASSESS ELIGIBILITY ................................................................................................................................................... 82
ACTIVITY: PREPARE AND SEND ACCEPTANCE PACK – VERIFY REPAYMENT AGREEMENT............................................. 83
ACTIVITY: PREPARE AND SEND HOME INSURANCE QUOTE................................................................................................ 83
ACTIVITY: TAKE FINAL DECISION .............................................................................................................................................. 84
TESTING THE WORK PORTAL.................................................................................................................................................... 87
Creating the users................................................................................................................................................................. 87
Running the application .................................................................................................................................................... 89
CONFIGURING THE SMTP SERVER ......................................................................................................................................... 92
CREATING THE EMAIL ACTIONS ................................................................................................................................................ 92
Reject application ................................................................................................................................................................. 95

Prepare and send acceptance pack ............................................................................................................................ 96
Prepare and send home insurance quote ............................................................................................................... 96
Notify applicant ..................................................................................................................................................................... 97
FINAL WORDS ............................................................................................................... Error! Bookmark not defined.
NEXT STEPS.................................................................................................................... Error! Bookmark not defined.

Final Project cuối kỳ

Copyright @bizagi    2

Introduction to Bizagi BPM Suite

Bizagi  BPM  Suite  is  the  leading  Business  Process  Management  (BPMS)  system  that  automates
processes  with  more  speed  and  flexibility  than  ever  before.  In  Bizagi,  most  of  the  common  and
reoccurring requirements in process automation have been prebuilt. That is why Bizagi delivers faster!

Furthermore,  Bizagi  empowers  business  users  to  automate  and  modify  complex,  dynamic  business
processes quicker and with more flexibility than any other solution, thus supporting the continuous
improvement of the organization’s critical processes.

Bizagi BPM Suite is composed of three tools that will help you manage the complete life cycle of a

business process: Model, Execute, and Improve.

Bizagi Process Modeler: The modeler enables you to visually diagram, model and document business
processes in industry-standard BPMN (Business Process Model and Notation). BPMN is a worldwide
accepted format for process modeling.

Bizagi  Studio:  The  construction  module  supports  the  definition  for:  the  data  model,  the  user
interfaces  (known  as  forms),  the  business  rules,  the  participants  or  performers  of  the  workflow
activities, and integration with external systems, amongst other things.

Bizagi BPM Server: The BPM Suite executes the model in a Work Portal, accessed through a browser
via the Bizagi BPM Server, for effective and intelligent process management. End users are presented
with a Work Portal to carry out their daily activities and to monitor business operations in real time
with a complete set of reports.

  3

Process Modeler

Bizagi Process Modeler provides:

•

Easy to use interface: An intuitive and easy to use interface that allows you to diagram from the

simplest to the most complex business processes.

•  Process documentation: Capability to publish high quality documentation in your preferred

format: Word, PDF, Web pages, SharePoint or Wiki.

•

Team Collaboration: Ability to collaborate with other team members during process definition.

Run discussions. Collaborate in the cloud or on premise. Work offline and sync when online
again.

•

Simulation: A powerful simulation engine that allows you to predict how your great ideas will

impact real-world businesses.

Bizagi BPM Suite
Once the process map is designed, access the Process in Bizagi Studio, where a user-friendly wizard
will walk you through all the necessary steps to turn your design into a running application.

Bizagi BPM Suite provides:

•  Control and visibility: Graphical real-time tracking and monitoring (who is doing what, when

and where). This feature ensures people execute according to the predefined workflow and

policies.

•  Alarms and notifications: Exceptions to service level agreements or non-compliance issues

generate alarms and are reported to the appropriate people.

•  Performance analysis and reporting: Out-of-the-box reports with deep insights into

operational performance (intelligent BPM or IBPM)

•  Auditing and traceability: Detailed log of performed activities – who changed what and when.

•  Workload routing and balancing: Graphical editor to define work allocation rules. This includes

load optimization algorithms and deals with delegates and working calendars.

•  Mobility: Stay connected to your business processes, be productive and take action while

onthe-go.

•

Extensibility and interoperability: Easy integration with applications such as SAP,

Documentum, SharePoint and mail.

•  Robustness: Secure, scalable and reliable workflow application (fault tolerant, clustering)

•  Quality: Solution tested in hundreds of implementations. There is no need to debug custom

software development code.

Final Project cuối kỳ

Copyright @bizagi    4

Description of the Loan Assessment Process

The Loan Assessment process takes place between an applicant and a loan provider, with the purpose
of approving loan applications. A BPMN representation of this process is provided in  Diagram 1.

This  process  is  executed  by  four  loan  provider  roles:  a  financial  officer  takes  care  of  checking  the
applicant’s  credit  history;  a  property  appraiser  is  responsible  for  appraising  the  property,  and  an
insurance sales representative is responsible for producing a home insurance quote, if required. The
loan officer, who is the applicant’s main point of contact, will perform all other activities.

The Loan Assessment process starts on receipt of a loan application submitted by an applicant. Once
the  loan  provider  receives  the  loan  application,  it  is  checked  for  completeness.  If  incomplete,  it  is
returned  to  the  applicant  to  fill the  missing  information  and  resubmit  it to  the  loan  provider.  This
process  is  repeated  until  the  application  is  received  complete  or  terminated,  which  occurs  if  an
application is not resubmitted within 5 days from the date of return to the applicant.

Next, the application must pass two checks to be approved: 1) the applicant’s loan risk assessment,
done automatically by a service, and 2) the appraisal of the property for which the loan is being sought,
carried out by a property appraiser. Before conducting the risk assessment, a financial officer performs
a credit history check on the applicant. After both the loan risk assessment and the property appraisal
have been done, a loan officer can assess the applicant’s eligibility. If the applicant is not eligible the
application is rejected; otherwise, the loan officer prepares an acceptance pack, prints it and sends the
hard copy to the applicant by post.

The acceptance pack includes a repayment agreement that the applicant must sign, and return to the
loan officer by post within two weeks. If received on time, the loan officer verifies that the applicant
has accepted the loan conditions and the repayment schedule of the agreement. Based on this check,
a different loan officer makes the final loan approval decision (i.e., the two-man rule is enforced). If
the  applicant  failed  to  accept  all  terms,  the  loan  officer  cancels  the  application;  otherwise,  it  is
approved. In either case, the process completes with the applicant being notified of the final result.

A loan application may be coupled with a home insurance plan, which is offered at a discounted price.
The applicant may express their interest in such a plan at the time of submitting their loan application.
This option is checked after sending the acceptance pack. If insurance is required, an insurance sales
representative will send a home insurance quote to the applicant. The acceptance of this quote by the
applicant and the associated insurance contract fall outside the scope of the Loan Assessment process.
Scope

This Process focuses on mortgage loan application processing, from receipt to approval.
Assumptions
•

The real-world process is collaborative, but to allow for simplicity of construction, we will regard
the process as non-collaborative. For this reason shapes showing interaction between processes,

•

•

such as message events, are replaced with different shapes.

The Loan Officer communicates via email with the applicant.

The Loan Officer receives the application form and enters the information in the Check

application form activity.

•

If the application is incomplete, a Timer event will be enabled that allows the Loan Officer to

resume the application once it is resubmitted via email.

•  All notifications to the applicant are sent via email.

  5

Quy trình đánh giá khoản vay

Mục đích của bài thực hành này là hướng dẫn cách sử dụng Bizagi để tự động hóa, chạy và giám sát
quy trình nghiệp vụ Đánh giá Khoản vay. Quy trình này được dựa trên các tài liệu của các tác giả Marlon
Dumas, Marcello LaRosa, Jan Mendling và Hajo A. Reijers. Thời gian thực hành khoảng 10-12 giờ.
Quy trình Đánh giá Khoản vay diễn ra giữa người nộp đơn và nhà cung cấp khoản vay, với mục đích
phê duyệt các hồ sơ vay vốn. Quy trình được biểu diễn bằng ngôn ngữ BPMN trong Sơ đồ 1.

Quy trình này được thực hiện bởi bốn vai trò của các nhân viên ngân hàng: nhân viên tài chính đảm
nhận việc kiểm tra lịch sử tín dụng của Người xin vay; một thẩm định viên tài sản chịu trách nhiệm
thẩm định tài sản và một đại diện bán bảo hiểm chịu trách nhiệm đưa ra một báo giá bảo hiểm nhà,
khi được yêu cầu. Cán bộ tín dụng, là đầu mối liên hệ chính của người nộp đơn, sẽ thực hiện tất cả
các hoạt động khác.

Quy trình Đánh giá Khoản vay được bắt đầu khi nhận được đơn xin vay do Người xin vay nộp. Sau
khi ngân hàng nhận được đơn xin vay, hồ sơ vay của khách hàng sẽ được kiểm tra để đảm bảo đầy
đủ các yếu tố cần thiết. Nếu không, hồ sơ được trả lại cho Người xin vay để điền các thông tin còn
thiếu và gửi lại. Quá trình này được lặp lại cho đến khi việc nhận đơn được hoàn tất hoặc chấm dứt,
điều này xảy ra nếu đơn không được nộp lại trong vòng 5 ngày kể từ ngày trả lại cho người nộp đơn.

Tiếp theo, đơn xin vay phải vượt qua hai lần kiểm tra để được chấp thuận: 1) đánh giá rủi ro khoản
vay của Người xin vay, được thực hiện tự động bởi hệ thống và 2) thẩm định tài sản mà khoản vay
đang được tìm kiếm, được thực hiện bởi người thẩm định tài sản. Trước khi tiến hành đánh giá rủi ro,
nhân viên tài chính thực hiện kiểm tra lịch sử tín dụng đối với Người xin vay. Sau khi cả đánh giá rủi
ro khoản vay và thẩm định tài sản đã được thực hiện, Cán bộ tín dụng có thể đánh giá tính đủ điều
kiện của Người xin vay. Nếu Người xin vay không đủ điều kiện, đơn xin vay sẽ bị từ chối; nếu không,
Cán bộ tín dụng chuẩn bị một hồ sơ chấp nhận, in và gửi bản cứng cho Người xin vay qua đường
bưu điện.

Hồ sơ chấp nhận bao gồm một thỏa thuận hoàn trả mà Người xin vay phải ký và gửi lại cho Cán bộ
tín dụng qua đường bưu điện trong vòng hai tuần. Nếu nhận được đúng hạn, Cán bộ tín dụng xác
minh rằng người xin vay đã chấp nhận các điều kiện cho vay và lịch trả nợ của thỏa thuận. Dựa trên
hồ sơ này, một Cán bộ tín dụng khác sẽ đưa ra quyết định phê duyệt khoản vay cuối cùng (tức là quy
tắc hai người được thực thi). Nếu người nộp đơn không chấp nhận tất cả các điều khoản, Cán bộ tín
dụng sẽ hủy đơn; nếu không, nó được chấp thuận. Trong cả hai trường hợp, quá trình hoàn tất với
việc người nộp đơn được thông báo về kết quả cuối cùng.

Đơn xin vay có thể đi kèm với gói bảo hiểm nhà, được cung cấp với giá chiết khấu. Người xin vay có
thể bày tỏ sự quan tâm của họ đối với kế hoạch đó tại thời điểm nộp đơn xin vay. Tùy chọn này được
chọn sau khi gửi gói chấp nhận. Nếu yêu cầu bảo hiểm, đại diện bán bảo hiểm sẽ gửi báo giá bảo
hiểm nhà cho người nộp đơn. Việc người xin vay chấp nhận báo giá này và hợp đồng bảo hiểm liên
kết nằm ngoài phạm vi của quy trình Đánh giá Khoản vay

Biết rằng:

• Cán bộ tín dụng liên lạc qua email với người nộp đơn.

• Cán bộ tín dụng nhận đơn vay và nhập thông tin trong quá trình Kiểm tra hồ sơ xin vay.

• Nếu đơn đăng ký chưa hoàn tất, hệ thống sẽ kích hoạt một sự kiện thời gian cho phép cán bộ tín
dụng theo dõi việc tiếp tục hoàn tất đơn xin vay sau khi nó được gửi lại qua email.

• Tất cả các thông báo cho người vay được gửi qua email.

Final Project cuối kỳ

Copyright @bizagi    6

Diagram 1. Loan Assessment process diagram

  7

I.  Create the project
Click the Bizagi icon on your desktop to open the application.  Select New to create a new Bizagi Project.

Name the project, LoanAssessment, and click Next.

Enter the following database credentials:

    Loginname: sa and Password: Bizagi10GO

 8

Bizagi will create the project, which may take a few minutes.

Once done Bizagi Studio will display a user-friendly wizard that will walk you through all the necessary steps
to turn your process map into a running application.

 9

II.  Model the process
Process modeling is the first step in the automation of a Process.

To create a process, go to Model Process in the Process Wizard and select New Process .

Type the name of the Process, Loan Assessment, and click Ok.

A Pool consisting of one Lane will load upon startup. Rename the Lane; double-click the Lane and type Loan

Officer.

   10

Add three more Lanes to the Process: Financial officer, Property appraiser and Insurance sales representative.

Drag and drop the Lanes from the Palette.

Drag and drop three Milestones to add phases. Rename them: Register, Assesment and Approval.

 11

Diagram the process flow by selecting all required shapes from the Palette and placing them in the  correct

position on the Process diagram.

All figures show a pie menu that allows easy selection of shapes for inclusion in the diagram. Icons for

manipulation of the shapes become visible when positioning the mouse over a figure.

To rename shapes and transitions, double-click on them and change their display name.

Important: All transitions must be properly connected and all the figures must be located inside Phases and

Functional Areas.

In the same way, add the remaining shapes until the diagram looks like Diagram 2.

   12

Diagram 2. Basic Loan Assessment process diagram

13

Convert Tasks, Events and Gateways to the proper types.

Right-click on the Assess loan risk Activity and transform it to a Service Task.

The three Notifications Activities, namely Send rejection message, Reject application and Notify applicant must
be transformed to Script Tasks.

Convert the Wait for 5 days Event to a Timer Event.

14

The Gateway preceeding the Timer Event must be an Event based Gateway.

The Check credit history and Appraise property Activities must enabled simultaneously. Also, the process cannot
continue until the Loan risk assessment and Property appraisal have been completed. To model this situation
convert the related gateways to a Parallel Gateways.

Finally, attach the Timer event to the Verify repayment agreement Activity. Right-click the Activity and select

Timer as the attached Event.

At this point, your Process should look like Diagram 3.

   15

Diagram 3. Complete Loan Assessment Process diagram

  16

Some parameters (properties) like the duration of Activites and Events must be set when the Process

diagram is complete. Set the duration of the timers as follows:

Event
Wait for 5 days

Verify
agreement

Duration (days)
5

repayment

14

To do this, right-click on the Timer Event and select Properties.

In the properties window enter the duration.

Lastly, save and close the Diagram Modeler windows to return to the Process Wizard.

17

III. Process data
Now that the Process Diagram has been created, we will proceed to the Data Model creation. The model

will include all the information required by the Process.

Bizagi provides a user-friendly wizard to build a structured data model with defined entities that allow the
data  to  be  created  only  once  and  used  throughout  the  process  and,  if  necessary,  be  reused  in  other
processes.   Most  entities  and  attributes  are  known  beforehand  at the  time of  defining the  case.  If  more
attributes or entities are needed, they can be included later in the design.

1.

In the second step of the Process Wizard, select Model Data.

2.  A pop-up window will display requesting the name of the Process Entity. The Process Entity is the

navigational starting point of the data model, that is the entity that gives access to all other entities in

the data model. Name it Loan Application and click Ok.

3.  Create the Master Entities. These are the business entities that store information which is directly and

exclusively related to each Process instance. To add a Master Entity, click the button located in the
Entity Bar called Master. Drag and drop the entity, and rename it.

18

Repeat the procedure for the remaining entities.

Entity

Description

Loan Application

Contains all information of the application.

Applicant

Reference

Holds  the  applicant´s  details  (identifying  particulars,  contact
details, financial information).

Contains  details  of  the  applicant´s  reference
particulars, contact details, financial information).

(identifying

Property Information

Contains the particulars of the mortgaged property.

Loan Information

Contains information of the loan (amount, number of years, start
date, interest rate, interest type)

Credit history report

Holds  information  relating  to  the  applicant´s  credit  history
(previous applications, overdue credits, current credi card).

Previous applications

Contains information of past applications made by the applicant
(loan type, amount, duration, interest rate).

Overdue credit accounts

Includes details on any overdue credit accounts held by the
applicant.

Property appraisal

Holds information on the appraisal of the morgaged property.

Surrounding properties

Contains information of surrounding properties. This information
is useful to appraise the mortgaged property.

Repayment agreement

Contains details on the repayment schedule (Monthly repayment
amount, Number of repayments).

19

Home Insurance quote

Holds  information  related  to  the  quote  of  the  home  insurance
(total cost, monthly payment)

Agreement summary

Contains  the  main  information  on  the  repayment  agreement
(Conditions agreed, digitized copy of the repayment agreement).

4.  Create the Parameter Entities. These entities store predefined values, or parameter values, that are

independent from the Processes’ execution. Parameter values cannot be modified or written to during

execution of a case.

Entity
Relation to applicant

Description

Possible  relationships  between  the  applicant  and  his/her
reference (e.g. parent, sibling, friend, etc).

Interest type

Interest rate types (i.e. fixed, variable).

Status

Loan type

Statuses of an application (i.e. completed, rejected, cancelled).

Types of loans (i.e. household, personal, domestic).

Credit assessment

Ratings that indicate credit quality (i.e. AAA,AA,A,BBB,BB,B).

Credit card provider

Accepted credit card providers (e.g. Visa, MasterCard).

Credit type

Property type

Types of credit (e.g. bank, consumer, investment).

Type of property (e.g. house, department, business premise).

20

To add a Paramenter Entity, click the Parameter button located in the Entity Bar. Drag and drop the

entity and give it a name.

Do the same for all the parameter entities. You may need to reorganize the entities as per your desire.

5.  Create the attributes, that is, the information that will be stored in each entity.

Right-click on the Loan Assessment entity and select Edit attribute list.

The Attribute List window, for the Loan Assessment entity, will display. Click the Add button to create

attributes; for each new attribute complete the following information:

•  Display Name: this is name that will be presented to the end user. It does not allow special

characters.

•  Name: this field will be automatically filled by the system and will be used for Business Rules.

•  Type: holds the data type of the attribute.

•

Length: determines the number of characters allowed in String data types.

21

The Loan application entity contains the following attributes:

Display Name

Application number

Submission date

Revision date

Type

Integer

Date-Time

Date – Time

Insurance quote required

Boolean

Risk weight

Status comments

Applicant eligibile?

Eligibility comments

Application complete?

Applicant

Reference

Integer

String

Boolean

String

Boolean

  Entity

-

-

-

-

-

-

-

-

-

Entity – Master

  Applicant

Entity – Master

  Reference

Property Information

Entity – Master

  PropertyInformation

Loan Information

Entity – Master

  LoanInformation

Credit history report

Entity – Master

  Credit history report

Property appraisal

Entity – Master

  Propertyappraisal

Repayment agreement

Entity – Master

  Repaymentagreement

Home insurance quote

Entity – Master

  Homeinsurancequote

Agreement summary

Entity – Master

  Agreement summary

Status

Loan Officer

Entity – Parameter

  Status

Entity -System

  WFUSER

22

Before creating these attributes take into account:

In order to find some attribute types (such as Float, Real, among others) you have to expand the  More

types node:

Entity – Master type attributes are attributes related to Master entities. To create these attributes

expand the Entity node, followed by the Master node and select the corresponding entity from the list.

Entity – Parameter type attributes are attributes related to Parameter entities. To create these

attributes expand the Entity node, followed by the Parameter three and select the desired entity from

the list.

23

Entity  –   System   type attributes are attributes related to Syste m entities.  T hese entities belong to the Bizagi’s
internal data model.  This   group of entities include s   information concerning the end user, areas, locations,
roles, skills among other s . To create these attributes ,   expand the  Entity   node ,  followed by   the  System   node ,
and   select  the  corresponding  entity from the list.

Collection  –  Master  type  attributes  are  attributes  with  a  one-to-many  relationship  to  a  Master  entity
(multiple relationship). To create these attributes expand the  Collection node, followed by the Master
node and select the desired entity from the list.

24

Once created, the attribute list for Loan Assessment will look as illustrated in the following screen.

Entity

Applicant

Attribute

Name

Sur name

Identification number

Type

String

String

String

Entity

-

-

-

25

Telephone number

Email address

Current address

Previous address

Duration of stay (years)

Current employer

Monthly incomes

Monthly expenses

Reference

Name

Sur name

Identification number

Telephone number

Email address

Address

String

String

String

String

Real

String

Currency

Currency

String

String

String

String

String

String

-

-

-

-

-

-

-

-

-

-

-

-

-

-

Relation to applicant

Entity - Parameter

Relationtoapplicant

Property Information

Property address

Purchasing price

Property type

Loan Information

Loan amount

Number of years

Start date

Interest rate

Interest type

String

Currency

-

-

Entity - Parameter

Propertytype

Currency

Real

Date - Time

Real

-

-

-

-

Entity - Parameter

Interesttype

Credit history report

Credit card start date

Date – Time

Credit card end date

Date – Time

Credit card interest rate

Real

-

-

-

Credit card provider

Entity - Parameter

Creditcardprovider

Credit assessment

Entity - Parameter

Creditassessment

Previous applications

Collection -Master

Previousapplications

Overdue credit accounts

Collection -Master   Overduecreditaccounts

Financial Officer

Entity -System

WFUSER

Previous applications

Amount

Currency

Duration (years)

Real

-

-

Loan type

Entity - Parameter

Loantype

Create the attributes for the remaining

Master entities.

26

Entity

Overdue
accounts

Attribute

credit

Default amount

Duration (years)

Interest rate

Credit type

Type

Currency

Real

Real

Entity

-

-

-

Entity - Parameter

Credittype

Property appraisal

Estimated commercial value

Currency

Comments

String

-

-

Surrounding properties

Collection -Master

Surroundingproperties

Property appraiser

Entity -System

WFUSER

Surrounding
properties

Address

Commercial value

String

Currency

Repayment agreement

Monthly repayment amount

Currency

Number of repayments

Integer

Repayment  agreement

File

Agreement summary

Conditions agreed

Repayment agreed

Repayment agreement (digital
copy)

Booelan

Booelan

File

Home insurance quote

Insurance cost

Currency

Additional monthly payment

Currency

Insurance quote

File

-

-

-

-

-

-

-

-

-

-

-

Sales representative

Entity -System

WFUSER

Also create the attributes for the Parameter entities.

Entity
Relation to Applicant

Interes type
Status
Loan type
Credit assessment

Credit card provider
Credit type
Property type

   Attribute
   Relation

Interest type

   Status
   Loan type
   Assessment

   Provider
   Credit type
   Property type

Type
String

String
String
String
String

String
String
String

27

Add values to the Parameter Entities. Right-click the Entity and select Values.

Click the Add…button to include values. The unique record identifier is generated automatically; you

only need to enter the description.

Enter the following values:

Entity
Relation to Applicant
Interest type

Status

   Attribute
   Relation

Interest type

   Status

Values
Parent, sibling, friend
Fixed, variable

Incomplete,complete,assessed,rejected,
cancelled, approved.

Loan type
Credit assessment
Credit card provider
Credit type

   Loan type
   Assessment
   Provider
   Credit type

Household, personal, domestic
AAA, AA, A, BBB, BB, B, Unrated
Visa, Master Card
Bank, consumer, investment

Property type

   Property type

House, department, business premise

Once complete, save and close the Data Modeler window to return to the Process Wizard.

At this point, the model should look like Data Model 1

28

Data Model 1. Loan Assessment data model.

29

IV. Forms creation
Once  the  Process  Diagram  and the  Data  Model  are  ready,  we  will proceed  to  create  the  forms  (user
screens) associated with each one of the human activities of the Process. Forms are used to enter and
display required information, so that end users may interact with the process.

In the Process Wizard, go to the third step of the Process Wizard: Define Forms.

In the new window, all activities without a form associated will be highlighted with an exclamation

mark. Click the desired activity to create its form.

Activity: Check application form
The first Activity of the Process, Check application form, must contain the following information:

Bài tập lớn cuối khoá

30

1.  Select the Activity Check application form. The Forms Designer window will display:

Bài tập thực hành

31

2.  Drag and drop five Groups, from the Containers menu located in the Controls tab, onto the

Display Area.

3.  Rename the groups to: Administration information, Applicant information, Reference Information,

Property information and Loan information. To do so, double-click the group, enter the desired
display name and select the Check icon.

Bài tập lớn cuối khoá

32

4.  Go to the Layout tab to alter the layout. Layouts enables you to design the form, specifically to

seperation of content into different columns to make it visually more appealing. Drag and drop

50%50% layouts into the DROP HERE section within the Groups.

5.  Click the Data tab in the left panel to add the data model attributes. Drag and drop elements from
the Data Model to the chosen layout section. To find attributes of related entities, expand the

Process Entity node.

Bài tập thực hành

33

6.  Once the required attributes have been included, define which of them will be mandatory. In this

activity all the attributes are required. To select multiple controls, click the first control and then

hold down the Ctrl key whilst you select the others.

In the left panel select Yes for the Required property to make all selected controls mandatory.

Bài tập lớn cuối khoá

34

For easy identification, the left border of a mandatory control is highlighted in red.

7.  Save the Form and close it to return to the diagram.

Activity: Check credit history
The activity form must contain the following information:

Bài tập thực hành

35

1.

In the third step of the Process Wizard, select the activity Check credit history. Drag and drop a Tab
control from the Containers section in the Controls tab, then click the Add icon (plus sign) to add
a new tab.

2.  Rename the tabs to Credit information and Application information.

3.  The Application information tab contains exactly the same information as the previously designed

form; duplicate the form by selecting the Copy From option.

Bài tập lớn cuối khoá

36

4.

In the new window select the activity from which to duplicate.  In this case, Check applicant

activity.

Click Ok.

5.  The form associated with the Check applicant activity will be copied onto the Application

information tab.  As this information is for the purpose of review only, change all controls on the

tab to be readonly.  As before, hold the Ctrl key to select multiple controls and then set the

Editable property to No in the Basic Properties panel.

Bài tập thực hành

37

6.

It is possbile to include all the attributes of an entity. Activate the Credit Information tab.  Locate

and right-click the Credit History report entity in the data model; select Add child elements to insert
all the attributes of this entity in the form.

7.

Include the necessary groups and reorganize the controls as in the image below.

Bài tập lớn cuối khoá

38

8.  Next, add columns to the tables. Select the Previous applications table and click the Edit columns

button.

9.  Navigate the data model (Note the view shows from the many entity of the collection), and select

the required attribute.  Drag it onto the Table control to become a column.

Bài tập thực hành

39

10.  Multi-select all columns in the table and make them read only.

11.  Repeat the steps to add columns to the Overdue credit applications table.

12.  Save the form and close it to return to the diagram.

Bài tập lớn cuối khoá

40

Activity: Appraise property
The activity form must contain the following information:

1.

In the third step of the Process Wizard. select the activity Appraise property.

2.  Create two tab controls: Property appraisal and Application Information.

3.  Follow the same steps used in the previous activity to replicate the Check applicant activity form

onto the Application Information tab.

Bài tập thực hành

41

4.  Move to the Property appraisal tab.  Locate the Property appraisal entity and add all attributes of

the entity in the form, using the Add child elements option.

5.  Next, add columns to the properties table and arrange the controls as shown below.

6.  Save the form and close it to return to the diagram.

Activity: Assess eligibility
The final form should look as below.

Bài tập lớn cuối khoá

42

1.

In the third step of the Process Wizard, select the activity Assess eligibility.

2.  Use the Copy From option to duplicate the Check credit history activity form on the Credit

Information tab.

3.  Create a new tab and name it Property Appraisal.

4.  Activate the Property Appraisal tab and copy the form associated with the Appraise property

activity.

Bài tập thực hành

43

5.  The form associated with the Appraise property activity containing two tabs namely, Property

appraisal and Application Information will be copied onto this form’s Property Appraisal tab. Drag

and drop the controls from the duplicated Property appraisal tab onto this form’s tab of the same

name.

6.  Remove the copied information that are not longer necessary.  In this case, the now empty

Property Appraisal and the Application Information tabs remaining from the duplicated form. To

do this, select each tab control and click the delete (red cross) icon.

Bài tập lớn cuối khoá

44

7.  Make all the controls of the form read-only, on all three tabs.

8.  Finally, navigate the data model and include the attributes pertaining to this form:  Risk weight,

applicant eligible and eligibility comments.

9.  Save the form and close it to return to the diagram.

Bài tập thực hành

45

Activity: Prepare and send acceptance pack
The final version of the form should look as below.

Bài tập lớn cuối khoá

46

In this activity the Loan Officer will generate a Repayment agreement. Bizagi will create the document

based on a predefined template, so it can be sent via email.

Download the template Repayment agreement.docx  from:

http://download.bizagi.com/

Save this file in a local folder for easy access.

1.  Select the activity Prepare and send acceptance pack in the third step of the Process Wizard.

2.  Copy the form associated with the Assess eligibility activity and make all the controls of the form

readonly.

3.  Switch the order of the first two tabs; drag and drop the Application information tab to the left.

4.  At the bottom of the Application Information tab, include a new group:  Loan repayment.

Also include the Monthly repayment amount and Number of repayment attributes and define them
as required.

5.  Recall that the Repayment agreement document will be generated using Bizagi’s Document

template functionality. Drag and drop a Document template control from the Bizagi controls

section in the Controls tab.

Bài tập thực hành

47

6.  Select the Document template control to access its properties.

•

•

Type Generate Repayment agreement as the button caption.

Select Repayment agreement as the data source (this attribute is located under the Repayment

agreement entity).

•  Make the control mandatory.

7.

In the Format tab, change the Display type to Value so that button caption will not display.

Bài tập lớn cuối khoá

48

8.  Next, configure the template. Return to the Basic tab and click Configuration Wizard to launch

the wizard

Click the Add icon alongside the Template control.

9.  Browse to the location where you previously saved the downloaded Repayment agreement

document, select it and click Next. Bizagi will upload the document as the template and name it

accordingly.

Finally, click Finish.

Bài tập thực hành

49

10.  Rename the document to Repayment agreement. This is the name that Bizagi will display for the

generated document.

11.  Next, click Add mapping to map the attributes from the Data Model to the template.

12.  On the left, you will find the attributes in Bizagi’s data model (Bizagi Data). The table on the right

shows all the tags used in the template. To map an attribute, click on the left table’s attribute and

then click on the right table’s corresponding tag.  Alternatively, drag the connection from the data

model attribute to the tag.

Bài tập lớn cuối khoá

50

13.  Minimize the window to exit full screen and click Finish. Click Ok to close the Configuration

wizard.

14.  Save the form and close it to return to the diagram.

Activity: Prepare and send insurance quote
The final form should look as below.

Bài tập thực hành

51

In this activity the Insurance Sales representative generates an Insurance quotation. Bizagi will create

the document based on a predefined template, so it can be sent via email.

Download the template Insurance quotation.docx from:

http://download.bizagi.com/

Bài tập lớn cuối khoá

52

Save this file in a local folder for easy access.

1.

In the third step of the Process Wizard, select the activity Prepare and send home insurance quote.

2.  Copy the form associated with the Prepare and send acceptance pack activity. Remove the

document template control  and then make all controls of the form read-only.

3.  Add a new group called Insurance quote to the Loan repayment section, at the bottom of the

Application Information tab. Also, include the Insurance cost, Additional monthly repayment and

Sales representative attributes.

4.  As before, a template will be generated using Bizagi´s document template functionality.

Repeat the procedure described in the previous activity to include a Document template control.

Create the following property definitions:

•

•

Set the button caption to Generate Insurance quote.

Select the Insurance quote attribute (found in the Home Insurance quote entity) as the data
source 

Set the Required property to Yes.

5.  Launch the Configuration Wizard and add Insurance quote.docx as the template.

6.  Rename it to Insurance quotation and map the attributes from the Data Model to the template as

follows:

Bài tập thực hành

53

7.  Exit full screen to click Finish.

8.  Save and close the form to return to the diagram.

Bài tập lớn cuối khoá

54

Activity: Verify payment agreement
The final form should look as below.

Bài tập thực hành

55

1.  Select the activity Verify payment agreement, in the third step of the Process Wizard.

2.  Duplicate the Prepare and send home insurance activity from. Remove the document template

control and make all controls read-only.

3.  Navigate the data model and locate the Agreement summary entity. Add the Conditions agreed,

repayment agreed and repayment agreement controls to the the Loan repayment group and make

them mandatory.

4.  Save and close the form to return to the diagram.

Activity: Take final decision
The final form should look as below.

Bài tập lớn cuối khoá

56

1.

In the third step of the Process Wizard, select the activity Take final decision.

2.  Copy the information from the Verify payment agreement activity. Make all controls on the form

readonly. In this activity we will include two buttons to allow the Loan Officer to approve or reject

the application. Enable the Form buttons option on the ribbon to display the button panel at the

bottom of the form.

Bài tập thực hành

57

3.  Click the Add icon to create a new button, select it to display its properties.

4.  Define the following Basic properties.

•

•

Button caption: Approve
Button execution: Rule 
Format:

o  Background color:
green o
Forecolor:

white

Action: Next 

Bài tập lớn cuối khoá

58

5.  Define the action to perform when the button is clicked.  Click the expression icon alongside the

Rule property to create a business rule.  The rule must set the status of this application to being

approved. Click the New button in the expression manager.

6.  First complete the basic information in the Properties tab: type a name, display name and

meaningful description. Right-click the arrow in the Design View and select Add assignment.

7.  Double-click to select the Assignment element and then choose Add to create a new assignment.

8.  Browse the variables list and select the Status attribute of the Loan Assessment.

9.  Click select entity value and then select Approved from the list of predefined values.

Select Ok to close each form and return to the Form Designer.

Bài tập thực hành

59

10.  Repeat the previous steps to create another button. Define the following properties:

•

•

Button caption: Reject
Button execution: Rule 
Format:

o  Background color:
red o
Forecolor:

white

Action: Next 

11.  Associate a rule with the Reject button. In the expression manager window type a name, display
name and description for the rule. Add an assignment element and set the Status attribute of the

Loan Assessment to the value of Rejected. Select Ok to close each form and return to the Form

Designer.

Bài tập lớn cuối khoá

60

12.  Finally, delete the  Save and Next buttons.

13.  Save and close the form and the diagram to return to the Process Wizard.

Bài tập thực hành

61

V.   Business rules

Process routing
The next step in the Process Wizard is the definition of business rules that control the process routing.
First,  we  will  assign  the  transition  rules. These  rules  evaluate  conditions  and  determine  which  control
flow should be used to continue the process. They are associated with the gateway shapes and return
Boolean values of true or false.

1.  To route the Process go to the fourth step of the Process Wizard and select Define Expressions.

2.  The expressions editor will open, highlighting the transitions that have no condition associated.

Gateways enable one or more paths according to business conditions. We will show how to define

expressions, to evaluate these business conditions, and determine which path the process has to

follow.

Bài tập lớn cuối khoá

62

Gateway 1. Form complete?

To identify if an application form is complete or not, the Application complete attribute is utilized. The

Loan Officer sets this attribute in the Check application form activity.

The Gateway evaluates the value of the Application complete attribute and enables one of two paths as

follows:

•

If the application form is complete, the process will continue to the Check credit history and

Appraise property activities.

•

If incomplete, the process will notify the applicant to make the necessary changes in the form.

To configure this evaluation follow the next steps:

1.  Click the transition named Yes that flows to the parallel gateway.

2.  Select the route based on the result of an expression. Click New to create a business rule.

3.

In the Boolean Expression editor, define the condition to be evaluated.

4.  Drag and drop the Application complete attribute, use the equal operator and select True as the

value of the condition. Consequently, the Yes sequence flow will be enabled if the Application

complete attribute is equal to true.

Bài tập thực hành

63

5.  Click Ok to save the rule.

6.  Now configure the other path.  This path will be followed when the business rule is NOT met, that

is, when the Application complete attribute is equal to False. Click the transition named No that

flows to the Send reject message task.

7.  The No transition should have the Else condition associated. Select the Else condition in the

Expression Selection window and then click Ok.

Bài tập lớn cuối khoá

64

Gateway 2. Applicant eligible?

The Applicant eligible attribute identifies if the applicant qualifies for the loan. The Loan Officer sets

this attribute in the Assess eligibility activity.

Based on the Applicant eligible value, the gateway enables one of two possible paths:

•

If the applicant is eligible, the process will continue to the Prepare and send acceptance pack

Activity

•

If the applicant is not eligible the process will notify the applicant that the loan has been
rejected.

To configure this evaluation follow the same logic used in the previous Gateway:

Select the Yes sequence flow and define the following condition.

For the transition named No, select the Else condition in the Expression Selection window.

Bài tập thực hành

65

Gateway 3. Quote requested?

The Insurance quote requested attribute indicates if a quote has been requested. The Loan Officer

assigns the value in the Check application form activity.

This gateway evaluates one of two possible paths based on the value entered in the  Insurance quote

requested attribute:

•

If a quotation was requested, the process will continue to the Prepare and send home

insurance quote activity.

•

If no request was made, the process will continue to the Verify payment agreement activity.

To configure this evaluation follow the same logic used in the previous gateway:

1.  For the transition named Yes define the following condition.

2.  Associate the Else condition with the No transition.

3.  Close the diagram to return to the Process Wizard.

Activity events
The Activity Actions option enables you to perform calculations and validations in every activity of the

process. These events can be executed when a token enters the activity, when the end user clicks on

the Save button, or when the token exits the activity.

Bài tập lớn cuối khoá

66

In this Process, we will use activity actions to automatically fill in known information:

•  Users working on a task: Loan Officer, Financial Officer, Insurance sales representative and

Property appraiser.

•  Revision date (the date on which the Loan Officer start working on an application).

•  Application status (set to the activity status that is active in the process).

•  Risk weight (defined according to the credit assessment).

Set Loan Officer and Revision date

1.  As details of the case creator is automatically retained in Bizagi, it can automatically filled.

Similarly, the Revision date can be set to the current date (today’s date).

2.

In the first activity select the On Enter option. Then click the Add icon to add an action in the

activity and then select Expression.

Bài tập thực hành

67

3.  Click New to create a new rule.

4.  The Expression editor will display. First complete the basic information in the Properties tab; this

information will let you identify the expression for reuse.

5.  Right-click the arrow in the Design View and select Add Expression. Type a name for the

expression:
Loan Officer and Date.

6.  Next, click Data Model to navigate the Loan Assessment entity and locate the Loan Officer

attribute.

Bài tập lớn cuối khoá

68

Click Ok.

7.  Click the Function option to view the set of Bizagi functions. Select the Case creator function

found in the Case creator user category. Click Ok.

Bài tập thực hành

69

At this point the expression should look like the example in the image below:

Follow the same logic to set the revision date:

Select the Revision date attribute from the Data model. Then

Select the Today function from the Date & time


type ‘=’ 
Category.

The final expression should look as follows:

Bài tập lớn cuối khoá

70

8.  Click Ok when done. Click Ok once more to save the Expression.

Set Loan Officer, Financial Officer, Property appraiser and Sales representative

1.  The details of Financial Officer, Insurance sales representative and Property appraiser are allocated
during different stages in the process. The current user of an activity is always known and can be
automatically filled.

2.  We will define the following rules:

Rule

Activity

Execution type

Set Financial Officer
Set Property appraiser   Appraise property

Check credit history

Set
representative

Sales

Prepare and send home insurance
quote

On enter
On enter
On enter

3.  To set the Financial Officer click the Check credit history activity, create an On enter expression and

add an expression module.

4.  Navigate the the data model and select the Financial Officer attribute.

5.  Choose the User id of current user function found in Current user information. Click Ok.

6.  The final expression should look like this example:

Bài tập thực hành

71

7.  The same logic can be used to set the Property appraiser in the Appraise property activity.

Finally, set the Insurance sales representative in the Prepare and send home insurance quote

Activity.

Set Status

The status of the application must be set in line with the active activity in the process flow. For example,
if the process enters the Check credit history activity, it logically follows the application is complete and
so its status can be set to complete.

We previously defined rules to set the status according to decisions made in the Take final decision

activity.

In this section, we will define the rules for the remaining statuses by creating the following activity

events.

Bài tập lớn cuối khoá

72

Rule

Set status to complete
Set status to incomplete

Activity – Event
Check credit history
Send reject message

Execution type
On enter
On enter

Set status to assessed

Assess eligibility

On enter

Set status to cancelled

Application cancelled

Set status to rejected

Reject application

On enter

On enter

1.  We will start with the first row of the table above and assign the status to complete.  Select the

Check credit history activity, create an On enter expression and add an assignment element as

shown.

2.  Add a new assignment and choose the Loan Assessment Status attribute from the variables list.

Select the Complete value from the associated entity values.

Bài tập thực hành

73

3.  Apply the same logic to define the remaining actions as set out in the table.

Set the Risk Weight

The risk weight must be set automatically according to the credit assessment as show in the next

table.

Credit assessment
AAA
AA
A
BBB

BB
B

Risk weight
100
80
60
40
20
0

We will use a policy action to assign the risk factor.

1.  Click the Assess loan risk Task and create a Policy action. Give the policy a display name, name and

meaningful description.

Bài tập lớn cuối khoá

74

2.

In the Policiy Manager window, click the New decision table option.

3.  Right-click the Xpath definition option and create a new definition.

4.  Give it a name and display name.

Bài tập thực hành

75

5.  Navigate the the data model and select the Credit Assessment attribute. Click Next.

6.  Mark the option This definition will be used to get a value option and then click Finish.

Bài tập lớn cuối khoá

76

The new definition will appear in the panel on the left.

7.  Repeat the steps to create another definition, this time select the Risk weight attribute from the

data model and again mark the This definition will be used to set a value option.

Bài tập thực hành

77

8.  Next, create the columns in the Decision Table.  To do this, drag and drop each definition onto the

design area on the right.

9.  Click the Add row option to insert the first row and duplicate the values as shown in the  Risk

weight table.

Bài tập lớn cuối khoá

78

10.  Duplicate the remainder rows and click Finish.

VI. Performers
The resources assignment is a very important stage within Bizagi.  The participants responsible for
each of the process activities are defined in this stage.

To allocate these performers we will use the same procedure as in the first workshop.

1. Click on the fifth step of the Process Wizard and select the Define Performers option.

Bài tập thực hành

79

The activities that do not have a performer configured are highlighted in the workflow.

For this process we will have five different allocations:

•

•
•

•

The activities Check application form, Assess eligibility, Prepare and send acceptance pack
and Verify payment agreement will always be performed by the case creator.

The Check credit history activity will always be executed by a Financial Officer.
The Appraise property activity will always be carried out by a Property appraiser.

The Prepare and send home insurance quote will always be performed by an Insurance

sales representative.

•

The Take final decision will always be executed by a Loan officer different from the officer

who verified the repayment agreement (i.e. following the two-man rule).

Activity: Check application form
This Activity must be assigned to the creator of the case; this is a default functionality Bizagi provides,
so  we  need  not  create  an  assignment  for  it  (despite  the  fact  that  the  activity  is  higlighted  with  an
exclamation mark).

Bài tập lớn cuối khoá

80

Activity: Check credit history
1.  Select the Activity and click on Add condition in the Performers assignment window.

2.  We need to add a performer holding a position of Financial Officer: Select Position in the first

dropdown list.

3.

In the Value field select Organization to be able to add a new position within the Organization.

Click New to add a new position within the Organization structure. Name it Financial Officer. Click

Save.

The final expression will look like this:

Bài tập thực hành

81

Activity: Appraise property
Select the Appraise property Activity and repeat the previous steps to add a new position within the
Organization structure called  Property appraiser.

Activity: Assess eligibility
1.  The Assess eligibility Activity is performed by the case creator.  That is the user identified as the
case creator of this activity.  Select the activity and add a new condition in the Performers
assignment window.

2.  Select User Id in the User Property drop-down.

3.  The list of Bizagi default expressions will display. Select the Case creator and click Ok.

Bài tập lớn cuối khoá

82

The expression will be assigned automatically to the task:

Click Ok to save the Performer Condition and again to save the performer.

Activity: Prepare and send acceptance pack – Verify repayment
agreement
1.  Select the activity in the process diagram.

2.  Repeat the previous steps to assign the case creator as the preformer for the Prepare and send

acceptance pack and Verify repayment agreement Activities.

Activity: Prepare and send home insurance quote
Follow the assignation steps in the Check credit history activity to create and assign the new position

of Sales representative.

Bài tập thực hành

83

Activity: Take final decision

1.  Select the Activity and click on Add condition in the Performers assignment window.

2.  Again, follow the assignation steps in the Check credit history activity to create and assign the new

position of Loan Officer.

3.  Click And to add another condition. Assign the Case creator as was done in the Assess eligibility

activity.

4.  The two-man rule denotes that the Loan officer must differ from the officer who verified the

agreement (the case creator); therefore, set the operator to Not equals.

Bài tập lớn cuối khoá

84

The Expression must look like this:

5.  Click Ok to save the Performer conditions.

Bài tập thực hành

85

VII. Execute
So far, the Process flow has been completed along with the structuring of the process information, the
user interface design for each one of the process activities, the definition of the business rules and the
performers.  We will now execute the automated process in the Work Portal.

The Work Portal enables participants in the process to see their pending activities, or inbox, as well as
realtime information relating to processes performance. Through color-coded indicators, alarms, and a
useful set of features you will be able to perform, manage and control your processes.

Click on the seventh step of the Process Wizard. In the new window select Run Process and then

Development.

Bizagi presents a work portal where the processes are interpreted and presented for end users.

Bài tập lớn cuối khoá

86

Testing the Work Portal

Creating the users

To test the Work Portal we have to create the end users. The following table presents the user list.

USER
LoanOfficer
Financial Officer

PASSWORD
Loanofficer
Financialofficer

DOMAIN   POSITION
LoanOfficer
domain
Financial Officer
domain

Property appraiser
Sales representative   Salesrep

Propertyappraiser

domain

domain

Property appraiser
Sales representative

LoanOfficer2

Loanofficer2

domain

LoanOfficer2

1.  Select the Admin Menu and click the Users option.

Click on New User and fill out the information from the user list table. Deselect all checkboxes:

Expired Password, Locked Account and Send Mail with Password to User.

Bài tập thực hành

87

2.  Move to the Organization tab and in the Positions field select Loan Officer. Click on Add to save

the user.

Do the same for the remaining users.

Bài tập lớn cuối khoá

88

Running the application

1.  Open the Work Portal, and login as the Loan Officer user.

2.  Create a new case for the process and test all the activites.

3.  Enter all the required and click Next.

Bài tập thực hành

89

4.  Note, the assignee is now the Financial Officer. Log out and log in as the Financial Officer.

Continue with the process flow entering the necessary information for each activity, as the

assignee. When the information is complete click Next.

5.

In the Prepare and send acceptance package activity you can click the Generate repayment
agreement button to generate the PDF document. The document will be generated and the link

inserted below the button. Click the document name to open it. Click Next

6.

In the Take final decision activity,  click the Approve button to approve the application and finish

the process.

Bài tập lớn cuối khoá

90

We have successfully tested our process.

Bài tập thực hành

91

VIII. Sending notifications (optional)
Emails, send during the Process life cycle, are easily configured in Bizagi.

Configuring the SMTP Server
To configure the SMTP server:

Go to the Configuration tab in Bizagi Studio and select Environment.

The Bizagi Environment Options window will display. Check the enable mail checkbox and fill in the
information for the SMTP server as follow:

•

•

SMTP Server: Your SMTP Server Name

SMTP Server Account: A Valid E-mail Account on the domain. It will appear as return

recipient of the emails sent.

Creating the email actions
To create email actions:

Bài tập lớn cuối khoá

92

1.  Go to the fourth step of the Process Wizard and select the option Activity Actions.

2.  Click on the Send rejection message Task and add an e-Mail on exit of the Task.

In the Definition Window, set the To field to the Email address of the LoanAssessment Applicant.

Enter the subject: Your application has been Rejected

Bài tập thực hành

93

Include the following text in the body of the email (Note the text within brackets are only to show

the location of the placeholders):

Dear (Applicant full name):

We  are  sorry  to  inform  that  your  Loan  Application  has  been  rejected.  The  reason  for  this
rejection as follow:

(Reject Reason)

3.  Next, we will include the placeholder attributes for applicant name and reject reason. Select the

XPath Field option. Navigate the Data Model and select the Name attribute. Click Ok. Note the

inclusion of the placeholder attribute in the body of the email. Do the same for the reject reason.

Your e-mail should look like this:

Bài tập lớn cuối khoá

94

4.  Click Save to close the e-mail Definition Window and then Ok on the Activity Actions Window.

5.  Repeat the previous steps to create the following emails:

Reject application

Bài tập thực hành

95

Prepare and send acceptance pack

Prepare and send home insurance quote

Bài tập lớn cuối khoá

96

Notify applicant

Bài tập thực hành

97

