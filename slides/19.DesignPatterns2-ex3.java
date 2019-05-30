interface User {
    public void print();
}

interface UserDetails extends User {
    public String getName();
    public String getAddress();
}

class DefaultUser implements UserDetails {
    private String name;
    private String address;

    public DefaultUser(String _name, String _address) {
	name = _name;
	address = _address;
    }

    public String getName() { return name; }
	
    public String getAddress() { return address; }
    
    public void print() {
	System.out.println(name);
	System.out.println(address);
    }
}

class VIP implements User {
    private UserDetails user;
    private String account;
    private Boolean prettyPrinting;

    public VIP(String _name, String _address, String _account, Boolean _prettyPrinting) {
	user = new DefaultUser(_name, _address);
	account = _account;
	prettyPrinting = _prettyPrinting;
    }
    
    public void print() {
	if (prettyPrinting) {
	    System.out.println("Name: " + user.getName());
	    System.out.println("Address: " + user.getAddress());
	    System.out.println("Account: " + account);
	} else {
	    user.print();
	    System.out.println(account);
	}
    }
}

class Main {
    static void printUser(User user) {
	user.print();
    }
    public static void main(String[ ] args) {
	DefaultUser user = new DefaultUser("sunghwan","SNU");
	VIP vip = new VIP("gil", "SNU", "1234", false);
	VIP vip2 = new VIP("hur", "KAIST", "5678", true);

	printUser(user);
	printUser(vip);
	printUser(vip2);
    }
}
