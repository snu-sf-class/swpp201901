// Singleton with lazy initialization
public class Singleton {
    private static class ResourceHolder {
        static final Singleton oneInstance = new Singleton();
    }
    public static Singleton getInstance() {
        return ResourceHolder.oneInstance;
    }
}
