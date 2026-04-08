import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {

    Calculator calc = new Calculator();

    @Test
    void testAddPositiveNumbers() {
        assertEquals(5, calc.add(2, 3));
    }
}
