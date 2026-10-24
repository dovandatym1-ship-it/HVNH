# Chapter03-EssentialProcessModeling

- **Tài liệu nguồn:** `Chapter03-EssentialProcessModeling.pdf`
- **Định dạng gốc:** `.pdf`
- **Công cụ chuyển đổi:** MarkItDown (Microsoft Open Source)
- **Thời gian chuyển đổi:** 2026-10-13 19:48:21

---

Chapter 3: Essential Process Modeling

Contents

1. First Steps with BPMN

2. Branching and Merging

3. Business Objects

4. Resources

5. Process Decomposition

6. Process Model Reuse

7. Recap

Process Modeling in the BPM Lifecycle

Examples for BPM lifecycle and process mining

35h

30h

B

15h

A

3m

5m

5m

D

10m

30m

E

2h

10m

!"#$%&&'
)(%,-).)$I-)#,

50%01"4"%.&6I)8"(("(

!"#$%"&'$($)%

!"*"+),&-.I0."12

34,+"4"%.&
-.I0."12

50%01"&;$(<

9)I"&6I)8"(("(

6I)8:I"
50."I$0+(

6I)8:I"
6I)=:8.(

50I<".
6I)=:8.(

!"+$*"I&
6I)=:8.(

50%01"&
9:(.)4"I&
-"I*$8"

!"#$%&&'I"$4)-%$-5"%

50%01"&6"I()%%"+

50%01"
3%#)I40.$)%&

50%01"&7((".(

-:,,)I.&6I)8"(("(

C

15m

1.5h

10min

?#,.#"1I,$%'I,('
2%".#"1I,$%'
),&)34-&

!"#$%&&'
()&$#*%"+

6&7)&'2"#$%&&
1#(%0

A

B

C

D

E

!"#$%&&
1#,)-#"),3

=>%$5-I<0%'
2"#$%&&
1#(%0

!"#$%&&
I,I0+&)&

8,&)34-&'#,
9%I:,%&&%&'I,('
-4%)"')12I$-

!"#$%&&
)120%1%,-I-)#,

;#7<%'2"#$%&&'
1#(%0

!"#$%&&
"%(%&)3,

Business Process Model and Notation (BPMN)

§ OMG standard (BPMN 2.1)
§ Supported by numerous tools: bpmn.org lists over 70 tools
§ Both for conceptual and executable models

BPMN from 10,000 miles…

Based on popular graphical flowcharts:

- Core set of notation elements

- Each core element has various subtypes

A BPMN process model is a graph consisting of four types of core elements:

start

end

activity

event

gateway

sequence
flow

Let’s start modeling

Order-to-cash

A typical order-to-cash process is triggered by the receipt of a purchase order from a
customer. The purchase order has to be checked against the stock regarding the
availability of the item(s) requested. Depending on stock availability the purchase order
may be confirmed or rejected.

If the purchase order is confirmed, an invoice is emitted and the goods requested are
shipped. The process completes by archiving the order or if the order is rejected.

Solution in BPMN: Order-to-cash

activity

2(#1'C.)(C0.C
'()$%

*#+#$(C)I-#I

!"#$"
"$%$&'$#

!"#$%C'()$%C
!"#$%C'()$%C
*+*,-*.,-,(/

split gateway

end
event

!"#$%&'(
)#*(#
#($(+,(*
start
event

2(#1'C0.
'()$%

!)./0I1C
)I-#I

!"#$
%#&'E#)*

!"#$%&''()

)"*+(,A
-"#A"

end
event

!"#A"
%&'%(''A#

Naming conventions

• Event: noun + past-participle verb (e.g. insurance claim lodged)

• Activity: imperative verb + noun (e.g. assess credit risk)

7

BPMN core elements

Activities capture work performed in a process

§ Different types of activities

Events represent the process’ triggers (start event)
and outcomes (end event).

§ Different types of events

activity

start
event

end
event

8

BPMN core elements

Gateways capture forking and joining paths in the control flow.

§ Different types of gateways

gateway

sequence
flow

Sequence flows represent the order in which activities and events
will be performed.

They can be assigned a condition to distinguish between alternative
branches.

§ Different types of flows

9

Process model vs process instances: The tokens game

Order #1
Order #2
Order #3

0#1#AEC)OP#O

=E#S'C4)ECI4C
'E)A%

>OP#O
O#1#AE#P

!"#A%C'E)A%C
*+*I-*.I-IE/

;<OA"*'#
)OP#O
O#A#I+#P

=E#S'CI4
'E)A%

!)4RIOSC
)OP#O

7SIE
CI4+)IA#

8"I9C:))P'

?OA"I+#
)OP#O

>OP#O
R<-RI--#P

10

A little bit more on events…

A start event triggers a new process instance
by generating a token that traverses the
sequence flow (“tokens source”)

An end event signals that a process instance has

completed with a given outcome by consuming

a token (“tokens sink”)

start
event

end
event

11

Let’s reconsider our order-to-cash example

If

the purchase order is confirmed, an invoice is
[…]
emitted and the goods requested are shipped. The
process completes by archiving the order. […]

0#1#AEC)OP#O

=E#S'C4)ECI4C
'E)A%

>OP#O
O#1#AE#P

!"#A%C'E)A%C
*+*I-*.I-IE/

;<OA"*'#
)OP#O
O#A#I+#P

=E#S'CI4
'E)A%

!)4RIOSC
)OP#O

7SIE
CI4+)IA#

8"I9C:))P'

?OA"I+#
)OP#O

>OP#O
R<-RI--#P

12

Solution: Order-to-cash

Anything wrong
with this model?

0#1#AEC)OP#O
0#1#AEC)OP#O

9E#S'C4)ECI4C
=E#S'C4)ECI4C
'E)A%
'E)A%

:OP#O
>OP#O
O#1#AE#P
O#1#AE#P

!"#A%C'E)A%C
!"#A%C'E)A%C
*+*I-*.I-IE/
*+*I-*.I-IE/

split

<SIECI4+)IA#

78OA"*'#
;<OA"*'#
)OP#O
)OP#O
O#A#I+#P
O#A#I+#P

9E#S'CI4
=E#S'CI4
'E)A%
'E)A%

!)4RIOSC
!)4RIOSC
)OP#O
)OP#O

7SIE
CI4+)IA#

8"I9C:))P'

;OA"I+#
?OA"I+#
)OP#O
)OP#O

split

="I>C?))P'

join

>OP#O
:OP#O
R<-RI--#P
R8-RI--#P

Mapping, Abstraction, and Purpose of a Model

Models are abstractions from real world phenomena,
developed for the purpose of reducing overall complexity.

Models aggregate information and document only relevant
aspects of the real world

Models are being developed:

1.

2.

in a specific modelling subject

for a specific target audience

3. with a specific modelling purpose in mind

14

What’s the relevant model?

?

15

A little more on gateways: XOR Gateway

An XOR Gateway captures decision points (XOR-
split) and points where alternative flows are merged
(XOR-join)

!"#$%&%"#

'(!"#$%&%"#

XOR-split è takes one outgoing branch

XOR-join è proceeds when one incoming branch
has completed

Example: XOR Gateway

Invoice checking process

5

Exercise 3.1

Model the following fragment of a business process for assessing
loan applications (loan origination process).

Once a loan application has been approved by the loan provider, an
acceptance pack is prepared and sent to the customer. The acceptance
pack includes a repayment schedule which the customer needs to agree
upon by sending the signed documents back to the loan provider. The latter
then verifies the repayment agreement: if the applicant disagreed with the
repayment schedule, the loan provider cancels the application; if the
applicant agreed, the loan provider approves the application. In either case,
the process completes with the loan provider notifying the applicant of the
application status.

A little more on gateways: AND Gateway

An AND Gateway provides a mechanism to
create and synchronize “parallel” flows.

AND-split è takes all outgoing branches

AND-join è proceeds when all incoming
branches have completed

Example: AND Gateway

Airport security check

Revised solution

Order-to-cash

0#1#A(C)OP#O

<(#S'C4)(CI4C
'()A%

=OP#O
O#1#A(#P

!"#A%C'()A%C
*+*I-*.I-I(/

XOR-split

7#4PCI4+)IA#

:;OA"*'#
)OP#O
O#A#I+#P

<(#S'CI4
'()A%

!)4RIOSC)OP#O

AND-split

AND-join

=OP#O
R;-RI--#P

7"I8C9))P'

>OA"I+#
)OP#O

Exercise 3.2

Model the following fragment of a business process for assessing
loan applications.

A loan application is approved if it passes two checks: i) the applicant’s loan
risk assessment, done automatically by a system, and ii) the appraisal of the
property for which the loan has been asked, carried out by a property
appraiser. The risk assessment requires a credit history check on the
applicant, which is performed by a financial officer. Once both the loan risk
assessment and the property appraisal have been performed, a loan officer
can assess the applicant’s eligibility. If the applicant is not eligible, the
application is rejected, otherwise the acceptance pack is prepared and sent
to the applicant.

22

Business Process Modeling Tools

Pen & Paper

Haptic

Standalone

§ E.g. Visio, Camunda Modeler

Repository-based

§ E.g. ARIS, Signavio, Apromore

XOR / AND are not always what we need...

Order distribution process

A company has two warehouses, one in Amsterdam, the other in
Hamburg, that store different products. When an order is received, it is
distributed across these warehouses: if some of the relevant products
are maintained in Amsterdam, a sub-order is sent there; likewise, if some
relevant products are maintained in Hamburg, a sub-order is sent there.
Afterwards, the order is registered and the process completes.

Solution 1

Order distribution process

XOR-split

XOR-join

AND-split

AND-join

Solution 2

Order distribution process

AND-split

AND-join

XOR-split

XOR-join

OR Gateway

An OR Gateway provides a mechanism to
create and synchronize n out of m parallel
flows.

!"#$%

!"#$#

OR-split è takes one or more branches
depending on conditions

OR-join è proceeds when all active
incoming branches have completed

27

Solution using OR Gateway

Order distribution process

28

What join type do we need here?

Exercise 3.3

Model the following fragment of a business process for assessing
loan applications.

A loan application may be coupled with a home insurance which is offered at
discounted prices. The applicants may express their interest in a home
insurance plan at the time of submitting their loan application to the loan
provider. Based on this information, if the loan application is approved, the
loan provider may either only send an acceptance pack to the applicant, or
also send a home insurance quote. The process then continues with the
verification of the repayment agreement.

Rework and repetition

Address ministerial correspondence
In the treasury minister’s office, once a ministerial inquiry has been received, it is
registered into the system. Then the inquiry is investigated so that a ministerial response
can be prepared.
The finalization of a response includes the preparation of the response itself by the
cabinet officer and the review of the response by the principal registrar. If the registrar
does not approve the response, the latter needs to be prepared again by the cabinet
officer for review. The process finishes only once the response has been approved.

XOR-join: entry
point

XOR-split: exit
point

Exercise 3.4

Model the following fragment of a business process for assessing
loan applications.

Once a loan application is received by the loan provider, and before
proceeding with its assessment, the application itself needs to be checked
for completeness. If the application is incomplete, it is returned to the
applicant, so that they can fill out the missing information and send it back to
the loan provider. This process is repeated until the application is found
complete.

32

Components of a modeling language

Modelling Language

Vocabulary

Syntax

Semantics

Notation

33

Components of a modeling language: Vocabulary

Modelling Language

Vocabulary

Vocabulary: set of modeling elements of
the language (BPMN: activities, gateways,
events…)

Syntax

Semantics

Notation

34

Components of a modeling language: Syntax

Modelling Language

Vocabulary

Syntax

Semantics

Notation

Syntax: set of rules to govern how these
elements can be combined (BPMN: start
events only have outgoing sequence flows
whereas end events only have incoming
sequence flows).

35

Components of a modeling language

Modelling Language

Vocabulary

Syntax

Semantics

Notation

Semantics: bind these elements, including
their textual descriptions, to a precise
meaning (in BPMN: activities model
something actively performed during the
business process, while XOR gateways
model exclusive decisions and simple
merging points).

36

Components of a modeling language: Notation

Modelling Language

Vocabulary

Syntax

Semantics

Notation

Notation: set of graphical symbols for the
visualization of the elements (in BPMN:
labeled rounded boxes to depict activities
and the circles with a thin border to depict
start events).

Business Objects (aka artifacts)

Can be:

§ Physical or digital information artifacts (e.g. an order on paper, an invoice on PDF)

§ Physical material (e.g. a box containing the ordered goods)

37

Our Order-to-cash process, again

!"#A%C'()A%C
*+*I-*.I-I(/

:;OA"*'#
)O4#O
O#A#I+#4

<(#P'CI0
'()A%

!)01IOPC
)O4#O

<(#P'C0)(CI0C
'()A%

R#S#A(C)O4#O

=O4#O
O#S#A(#4

7#04C
I0+)IA#

7"I8C9))4'

>OA"I+#
)O4#O

=O4#O
1;-1I--#4

The purchase order document serves as an input to the stock
availability check against the Warehouse DB. Based on the
outcome of this check, the status of the document is updated,
either to “approved” or “rejected”. If the order is approved, an
invoice and a shipment notice are produced. The order is then
archived on the Orders DB.

38

Business Objects in BPMN

*+IE-./)
'I0)I

1%&'#E)

!"#$
#%&'#E)

A Data Object captures an artifact required
(input) or produced (output) by an activity.

§ Can be physical or electronic

A Data Store is a place containing data
objects that must be persisted beyond the
duration of a process instance.

It is used by an activity to store (as output)
or retrieve (as input) data objects.

/$.()"'M!1

M)%"*#'%*+,

!"#$%"C"'()%"*#'
%*+,$-.#%,*

39

Solution

!"#$%&'(
)#*(#

!"#$%&'(
)#*(#
+$%($,(*-

<(#P'CI0
'()A%

!)01IOPC
)O4#O

!"#A%C'()A%C
*+*I-*.I-I(/

:;OA"*'#
)O4#O
O#A#I+#4

<(#P'C0)(CI0C
'()A%

R#S#A(C)O4#O

!"#$%&'($)*+

!"#$%&'(
)#*(#
+#(,($-(*.

!"#$%&'(
)#*(#
+&,,#-.(*/

!"#$%&'

7#04C
I0+)IA#

7"I8C9))4'

!"#$%&'(
)#*(#
+&,,#-.(*/

>OA"I+#
)O4#O

=O4#O
1;-1I--#4

=O4#O
O#S#A(#4

!"#$"%&'(

!"#$%&'(
')(#*&

The purchase order document serves as an input to the stock availability check against the Warehouse
DB. Based on the outcome of this check, the status of the document is updated, either to “approved” or
“rejected”. If the order is approved, an invoice and a shipment notice are produced. The order is then
archived on the Orders DB.

40

Exercise 3.5

Is there any missing data
object or data store in the
example below?

BPMN Text Annotations

A Text Annotation is a mechanism to provide additional text information to the model
reader

§ Doesn’t affect the flow of tokens through the process

*+I-.(/)%$0I10&#+&

/*%C0"*12#FC+('*+1#.

!"#$%&''()

!"#$%C'#(F*%C
"+(#C+,#-.

42

Exercise 3.6

Put together the four fragments of the loan assessment process that
you created in Exercises 3.1–3.4.

Hint. Look at the labels of the start and end events to understand the order
dependencies among the various fragments. Then extend the resulting
model by adding all the required business objects. Moreover, attach
annotations to specify the business rules behind i) checking an application
completeness, ii) assessing an application eligibility, and iii) verifying a
repayment agreement.

Resources

Active resources:

§ Process participant
§ Software system
§ Equipment

Resource class:

A group of (active) resources that are interchangeable, e.g. a role, an
organizational unit or the whole organization.

44

Resources in the order-to-cash example

The order-to-cash process is carried out by a seller’s organization which
includes two departments: the Sales department and the Warehouse &
Distribution department.

The purchase order received by the Seller has to be checked against the
stock. This is done via an ERP module within the Warehouse &
Distribution department.

If the purchase order is confirmed, the Warehouse & Distribution
department ships the goods. Meantime, the Sales department emits the
invoice. The process concludes with the order being archived by the Sales
department.

45

BPMN Elements – Pools & Lanes

Pool
Captures a resource class. Generally used to model a business party (e.g. a
whole company)

#

"
"
!

Lane
Captures a resource sub-class within a resource class by partitioning a pool.
Generally used to model departments (e.g. shipping, finance), internal roles (e.g.
Manager, Associate), software systems (e.g. DBMS, CRM) or equipment (e.g.
Manufacturing plant)

$%&'

#

"
"
!

$%&'

$%&'

$%&'

46

Solution: Order-to-cash

14

Exercise 3.7

Extend the business process for assessing loan applications that you
created in Exercise 3.6 by considering the following resource
aspects.

The process for assessing loan applications is executed by four roles within
the loan provider: a financial officer takes care of checking the applicant’s
credit history; a property appraiser is responsible for appraising the property;
an insurance sales representative sends the home insurance quote to the
applicant if this is required. All other activities are performed by the loan
officer who is the main point of contact with the applicant.

Exchanging information between business parties

Order-to-cash

The purchase order sent by the Customer is received by the Seller and
checked against the stock. This is done via an ERP module within the
Warehouse & Distribution department. If the purchase order is not
confirmed, the Sales department sends an order rejection to the
Customer, otherwise it sends an order confirmation.

Next, the Warehouse & Distribution department ships the goods and sends
a shipment notification to the Customer. Meantime, the Sales department
emits the invoice and sends it to the Customer. The process concludes
with the order being archived by the Sales department.

49

BPMN Elements – Message Flow

A Message Flow represents a flow of information or materials between
two process parties (Pools)

!"##$%"

A Message Flow can connect:
• directly to the boundary of a Pool è captures a message to/from that party
•

to a specific activity or event within that Pool è captures a message that triggers a
specific activity/event within that party

!""#$%

&
$
#
"
"
!

!"#$

!"#"$%"

%
$
#
"
"
!

&
$
#
"
"
!

!"#"$%"

!"#$

50

BPMN Elements – Start Message Event

The start message event triggers a process by the receipt of a message
when an incoming message flow is connected to the event

!"##$%"

!"##$%"
&"'"()"*

51

Solution: Order-to-cash

52

Pools, Lanes and Message Flows: syntax

1. The Sequence Flow cannot cross the boundaries of a Pool
2. Both Sequence Flow and Message Flow can cross the boundaries of Lanes
3. A Message Flow cannot connect two flow elements within the same pool

19

When are messages sent or received?

• A Send activity will send the outgoing message upon activity

completion

• A Receive activity won’t start until the incoming message has been

received

!""#$%

&
$
#
"
"
!

!"#$

!"#"$%"

%
$
#
"
"
!

&
$
#
"
"
!

!"#"$%"

!"#$

Note: the order of the message flows w.r.t. an activity is irrelevant, the
above rules always hold

54

When are messages sent or received?

• Message B is first received
before Activity can start.
• Message A is sent after,

upon Activity’s completion

•

•

First, message B is
received, before Activity can
start.
Then, message A is sent,
upon Activity’s completion

55

Process (or Orchestration) Diagram

Models a single business party and can be:
Public view (black box)

%

+
#
-
,
+
*
)
(
'
'
&
%
A
#
"
!

%

Private view (white box)

56

,-%#+
+
)*
(
%'
'
#A%C
"
!

4C'."#A)/"#A%C'

*+'.)/"#A%C')
#,+/A%C')
#C'0%,1/A%C'

*+'.)/"#A%C')
#C15S+A%C')
'CA%0%#/A%C'

*+'.)/"#A%C')
#,+/A%C')
#C'0%,1/A%C'

!"#A%C'
2+(%'3

Collaboration Diagram

Models a global business process between at least two business parties (each
modelled by a Pool)

!"+S-S"#)."A5-
+G()2)D/()G+

!"+S-
;/5P"+(-
S"(/)#1

!"+S-
;/5P"+(-/D8<

4/5P"+(
S"(/)#1

4/5P"+(
/D8+G9#"S,"P"+(

=GGS1
1"+(
+G()2)D/()G+

7"#)."A5
/D8+G9#"S,"P"+(

!"+S-/CD()G+-
DA"/()G+-
A"0C"1(

BCD()G+
DA"/()G+
A"0C"1(

BCD()G+
DA"/()G+
DG+2)AP/()G+

BCD()G+
DGP;#"()G+
+G()2)D/()G+

?G+SCD(-/CD()G+

!"+S-/CD()G+-
DA"/()G+-
DG+2)AP/()G+

!"+S-/CD()G+-
DGP;#"()G+-
+G()2)D/()G+

!"+S-/CD()G+-
DA"/()G+-
DG+2)AP/()G+

BCD()G+
>",)+1

:)S

:)S
/D8+G9#"S,"P"+(

BCD()G+
DGP;#"()G+
+G()2)D/()G+

A
##"
"
!

"
)D
A.
"
-!
,
)+
+
()G
D
C
B

A
"
S
)S
:

57

Private
process

Public
process

Exercise 3.8

Extend the model of Exercise 3.7 by representing the interactions
between the loan provider and the applicant.

Process decomposition

60

Process decomposition

An activity in a process can be decomposed into a “sub-process”

!"#$%&'&E)*+,#-./'00

!"#$!"#$

!"##$%C'()
*+,-%."/'CC

Activities

Use this feature to:

1.
2.

Improve understanding by breaking down large models
Identify parts that should be:

§ repeated
§ executed multiple times in parallel
§ interrupted, or
§ compensated

61

Example: Sub-Process

E)*#+$BD
"B$B+*B5

!"#$BCCD
E)*#+$B

!"#$BCCD
!N;MB)2

!"#$BCCDE)*#+$B

)#D
M+CMN2$-BC

P)2B"DE)*#+$BD4D
I"B5+2D6#2BD
7B2N+8C

I-B$.DE)*#+$BD
/+CMN2$-BC

M+CMN2$-D
B9+C2C

:8#$.DE)*#+$B

62

Identify possible sub-processes

Acquire raw materials

Ship and invoice

63

Solution

64

The refactored model

Exercise 3.9

Identify suitable sub-processes in the process for assessing loan ap-
plications modeled in Exercise 3.6.

Hint. Use the building blocks that you created throughout Exercises
3.1–3.4.

66

Imposing order of messages via subprocess

The expanded subprocess for “Activity”

67

Example: Modelling process hierarchies

:#-#1C;

>'I$#66C
?L@R)'AC.LEC
BRI*#

+#$#)-#C.LEC
0.1)E.*#C
O'E#'

PPP

:#-#1C<

QL*#'CO'E#'

!"#$%C!'#E)*

O'E#'C
'#$#)-#E

:#-#1C=

!"#$%C!'#E)*C
+#$I'E

!'#E)*C
.-.)1.V1#

!'#E)*CLI*C
.-.)1.V1#

!1#.'CO'E#'

!IL*.$*C
$R6*I7#'C
.$$IRL*C'#8P

PPP

PPP

(Fragment of the SCOR reference model)

68

Value chain modelling

Chain of (high-level) processes an organization performs in order to achieve a business goal,
e.g. deliver a product or service to the market.

Business
process

“is predecessor
of”

69

Linking value chains with process models

Process
model for
this process
is available

70

Guidelines: modeling levels

Use sub-processes when the model becomes too large:

§ Hard to understand
§ Increased error probability

Level 1 – start with value chain

Level 2 – add main decisions and handoffs (lanes)

Level 3+ – add procedural aspects:

§ Parallel gateways
§ Data objects, data stores
§ Exception handling
§ And as much detail as is relevant

Decomposition drivers:

§ Logical: group elements meaningfully (e.g. common business object)
§ Structural: up to 30 nodes (activities, events, gateways)

Process Reuse

By default, a sub-process is “embedded” into its parent process (i.e. it is stored
within the same file)

In order to maximize reuse, it is possible to “extract” the sub-process and store it as
a separate file in the process model repository

Such a sub-process is called “global” model, and is invoked via a “call” activity

(normal)
activity

Call
activity

72

Example: process reuse

Call activity is the
default choice to
maximize reusability

Exercise 3.9

Identify suitable sub-processes in the process for assessing loan ap-
plications modeled in Exercise 3.6.

Hint. Use the building blocks that you created throughout Exercises
3.1–3.4.

74

Sub-processes: syntax

Sequence flows cannot cross sub-process boundaries

§ Use start/end events

Message flows can cross sub-process boundaries

§ To indicate messages emanating from/incoming into the sub-process

Start with at least one start event

§ If multiple, first occurring will trigger the sub-process

Finish with at least one end event

§ The sub-process will complete once all tokens have reached an end event.

May need an (X)OR-split after sub-process to understand what end
event(s) have been reached

75

Example: sub-process with multiple end events

Quote-to-order

Exercise 3.10

Identify suitable sub-processes in the process of Exercise 1.7 (page
30). Among these sub-processes, identify those that are specific to
this process versus those that can potentially be shared with other
processes of the same company.

Recap

1.

2.

BPMN activities capture units of work in a process

Events define the start and end of a process, and signal something that happens
during the execution of it

3. Gateways model exclusive and inclusive decisions, merges, parallelism and

synchronization, and repetition

4.

A process model depicts all the possible ways a given business process can be
executed, while a process instance captures one specific process execution out of all
possible ones

5. Data objects capture a physical or digital business object required to execute an

activity or trigger an event, or that results from the execution of an activity or an event
occurrence

6.

7.

Pools generally model resource classes while lanes are used to partition pools

Sub-processes represent activities that can be broken down in a number of internal
steps, as compared to tasks, which capture single units of work

