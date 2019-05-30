interface User {
    public void print();
}

class DefaultUser implements User {
    private String name;
    private String address;

    public DefaultUser(String _name, String _address) {
	name = _name;
	address = _address;
    }
    
    public void print() {
	System.out.println(name);
	System.out.println(address);
    }
}

class VIP implements User {
    private DefaultUser user;
    private String account;

    public VIP(String _name, String _address, String _account) {
	user = new DefaultUser(_name, _address);
	account = _account;
    }
    
    public void print() {
	user.print();
	System.out.println(account);
    }
}

class Main {
    static void printUser(User user) {
	user.print();
    }
    public static void main(String[ ] args) {
	DefaultUser user = new DefaultUser("sunghwan","SNU");
	VIP vip = new VIP("gil", "SNU", "1234");

	printUser(user);
	printUser(vip);
    }
}
