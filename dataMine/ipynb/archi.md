选择题 40 分 主要是 EJB 和 JPA 的部分，下面给的是一些我在网上做的练习题和答案，如果有相同题目最好，没有就蒙吧
1 有状态 bean 的生命周期状态是：dose not exist,method ready,method ready in transaction,passive 
2 无状态 bean 的生命周期状态是：dose not exist,method ready pool 
3 实体 bean:pooled,ready
4 what is the sequence of steps in the life cycle of a stateless session bean? class.newInstance().setSessionContext(ctx),ejbcreat() 
5 HTTPS is Http over ssl and http is
connection base and stateless 
6 Asynchronous communication is achieved by using Message Oriented Middleware,Decentralized messaging using Secure Sockets Layer is not part of Messaging architecture.
7 in P2P,client send message to A designated queue.
8.Security is an Architecture non-functional requirement and the mandatory checking account a functional design
requirement.
9.what non-functional requirements were discussed?Performance,availability,scalability and security 
10if a computer can have exactly 1 processor,1 HDD and 1 memory
stick,what pattern would be best used here? Builder 
11.in which of the following cases would an application not necessarily benefit from the use of EJB? Small scale deployment and no
transactional requirements 
13.The container applies what memory management techniques in the case of Session beans?Bean pooling and bean passivation 
14.what happens when the
remove() method is called on the home interface of an entity bean?the remote reference is invalidated and the data represented by the bean instance id deleted from the database. 
16.which two improve software maintainability？ Code factoring and reusing components .
17what decreases software maintainability?Data sharing and high coupling .18whilch two features of a
firewall might interfere with the operation of IIOP?Port filtering and address filtering 
20.As an architecture,you are interested in the architecture characteristics of a system.which two are
architectural characteristics? Reliability and performance.
21.which two statements are true about management of an EJB’s resources? The reference to home object is obtained through JNDI
to improve maintainability and flexibility and the EJB container can manage the instance’s access to its resourced because the remote object acts as a proxy. 
24.what is benefit of bean
poolong in an EJB container?it reduces the memory allocation and garbage-collection cycles. 
25.which statement about an EJB container’s life-cycle management of session beans is true?the
container can passivate a stateful session bean to free limited resources. 
26.what statement aboutpassivating beans is true?the passivated stateful session bean should close all
connections before being passivated
17.How would you encapsulate interaction with that legacy system?with an ejb session bean that uses JMS to message the legacy system. 
18.which three
statmentsaboutcontainer-managedpersistencearetrue?acontainer-managedenterprisebeanrequireslesscode,container-managedpersistenceprovideslessbean
control,container-managed persistence an require complex mapping techniques.
19.what acts a proxy to an EJB? Remote instance.
30.what is an alternative solution?use a stateful session
bean as a Mediator to the entity beans.
31.a client makes a transcationless method call an EJB that has a transaction attribute of required in the deployment descriptor.which state is true?the
container creates a new transaction.
31.which two statements about stateless session beans are true?they provide a generic service and they may provide high performance by being
available for multiple clients.
32.which pattern provides a means to access the elements on an aggregate object sequentially without exposing the undelying structure?literator.
33.which
pattern will solve the problem?Mediator.
34.what are two benefits of the Facade pattern?it hides complex subsystem from client and it encourages weak coupling between the client and the
subsystem.
35.which design pattern is represented by EJB Home Interface?abstract factory.16.what are three benefits of design pattern?they act as a learning aid,they provide a common
design vocabulary,they standardize the way designs are developed.
17.what are two clear advantages to using message services in an application?Provides scalability ,allows loose coupling
between components.
18.which two statements about JMS are true?JMS supports Publish/Subscribe,JMS uses JNDI to find the destination.
40.which three architectural decisions adhere to he
requirements?(3)Make Order and account an entity EJB,Make customer a staeful-session EJB,make customer a session EJB and put business logic in it 
41.which two services dose EJB
provide?Transaction services,Life-cycle management..42.what types of EJB cannot use bean-managed transaction demarcation?BMP entity bean,CMP entity bean.
43.Given an Order entity
EJB and a single class loader, which of the following is a Singleton?OrderBemote 
44.An EJB is required to process credit card purchases. All purchase-related information such as card number
and amount will be supplied as parameters to a single business method invocation that processes the purchase. Server performance is critical. Which bean type BEST suits the
requirement? A stateful session bean45.A container-managed persistence (CMP) bean A has a one-to-many container-managed relationship (CMR) with another container-managed
persistence (CMP) bean B. Select the interface that will expose the methods related to this relationship. The home interface of bean A.
46.Which of the following represent valid state
transitions through an EJB method for a CMP entity Bean, according to its life cycle? "Does Not Exist" to "Pooled" via Class.newInstance() then setEntityContext(), "Pooled" to "Ready" via
ejbCreate() then ejbPostCreate()
47.A JMS session can implement:the TopicSession interface to support the publish-subscribe model,the QueueSession interface to support the
point-to-point model.
48.Which of the following is NOT a required step to get a reference to an existing EJB's home?Use the RMIRegistry lookup() method to get a remote reference to the EJB
home.
48. A stateful session bean is to be created. Which of the following objects are necessary?home interface,bean class, component interface
49.Given that a data source "FinanceDB" is
already registered with JNDI, what are the steps that a JDBC application needs to take to create a connection to the database? "FinanceDB"Context ctx = new InitialContext(); DataSource ds =
(DataSource)ctx.lookup("java:comp/env/jdbc/FinanceDB"); Connection con = ds.getConnection("j2ee", "hello");
50.An EJB that is deployed with container-managed transaction demarcation
has a business method that performs an operation that might throw a checked exception. The bean cannot recover from this checked exception and should rollback. Which implementation
accomplishes this with the least amount of code and a maximum of information for the EJB client? public void businessMethod() throws EJBException {try {// operation throwing
SomeCheckedException goes here} catch (SomeCheckedException ae) {context.setRollbackOnly();throw new EJBException(ae);}}
51.A CMP entity bean implements a BankAccount record. The
bean requires a composite primary key consisting of a branch number and an account number. Both values are of type int. The class AccountKey has been created to hold these values. Which
of the following declarations of ejbCreate() would be valid ways to create a BankAccount bean, given that neither field can be automatically generated ?ejbCreate(int branchNumber, int
accountNumber), ejbCreate(AccountKey key)
52.Which of the following method declarations would MOST likely be found in the remote home interface of the entity bean named
Customer?CustomercreateWithSSN(intid,StringsocialSecurityNumber)throwsCreateException,RemoteException;CollectionfindAllByAge(intage)
throws FinderException, RemoteException;
52.In a Web application where performance is key, JDBC is used to query a database. The database is queried with parameters that are specified by
users on a form. Which of the following are valid? aPreparedStatement.setString(2, "data");,aStatement.setString(2, "data");53.Which of the following are not considered tiers in a J2EE based
n-tier model?EJB Integration Tier,Legacy Connectivity Tier
55.Which of the following are not service level requirements that affect software architecture?detailed Design,Training,Design
patterns
55.Which of the following statements are true about the Entity class?Entity class must be declared as top level class,Enum can be declared as Entity56Which of the following are
correct?@entity public class employees{..},public class employees implements serializable{...}
57If you want to send an entity object as the pass by value through a remote interface, which of
the following statements are valid?@entity public class employees implements serializable{...}
58. Which of the following statements are correct?all the above 
59Which of the following
statements are correct?Entities supports inheritanc e,Abstract class and concrete classes can be entities,Instance variables of an entity class must be private,protected or package visibility60
Which of the following statements are correct?Every entity must have a primary key
61.Select the valid primary key types?all the above
62.Which of the following are true about composite
primary keys?All the above63.Which of the following are not true about composite primary keys?The primary key class may not define equals and hashCode methods,May not have public
no-arg constructor.
