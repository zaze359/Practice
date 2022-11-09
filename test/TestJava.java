package test;

import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;

public class TestJava {
    // private static final String name = "张三";
    // private static final String name = "张三";
    // private static String name = "张三";
    // private static final String name = new String("张三");

    private static String name = "张三";

    static class A {
        private final String name = "张三";
        public String getName() {
            return name;
        }
    }

    static class B extends A{
        private final String name2 = "张三";
        public String getName2() {
            return name2;
        }
    }

    public static String getName() {
        return name;
    }

    public static void main(String args[]) {
        System.out.println("before: " + name);
        try {
            A a = new A();
            Field nameField = A.class.getDeclaredField("name");
            // 修改nameField中的modifiers，去除final
            Field modifiersField = Field.class.getDeclaredField("modifiers");
            modifiersField.setAccessible(true);
            modifiersField.setInt(nameField, nameField.getModifiers() & ~Modifier.FINAL);
            //
            nameField.setAccessible(true);// 不能少
            nameField.set(a, "李四");
            System.out.println("field: " + nameField.get(a)); // 输出李四
            System.out.println("name: " + a.name); // 张三
            System.out.println("getName: " + a.getName()); // 张三

            B b = new B();
            Method[] methods = b.getClass().getDeclaredMethods();
            // Method[] methods = b.getClass().getMethods();
            for(Method method : methods) {
                System.out.println("method: " + method.getName());
            }
            System.out.println("method: " + b.getClass().getMethod("getName").getName());

            Field[] fields = b.getClass().getDeclaredFields();
            // Field[] fields = b.getClass().getFields();
            for(Field field : fields) {
                System.out.println("field: " + field.getName()); 
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        // Node node = new Node(16);
        // System.out.println("node: " + node.forwards[0]);
    }

    public static class Node {
        private int data = -1;
        private Node forwards[];
        private int maxLevel = 0;

        public Node(int level) {
            forwards = new Node[level];
        }

        @Override
        public String toString() {
            StringBuilder builder = new StringBuilder();
            builder.append("{ data: ");
            builder.append(data);
            builder.append("; levels: ");
            builder.append(maxLevel);
            builder.append(" }");
            return builder.toString();
        }
    }
}
