#include <iostream>
#include <string>
class Car
{
public:
    std::string brand;
    int speed;
    bool engineRunning;
    Car(std::string b, int s) : brand(b), speed(s), engineRunning(false)
    {
        std::cout << "Car created! Brand: " << brand << ", Speed: " << speed << " km/h\n";
    }

    void startEngine()
    {
        if (!engineRunning)
        {
            engineRunning = true;
            std::cout << "Engine started! Let's make cars great again!\n";
        }
        else
        {
            std::cout << "Engine is already running... were winning!\n";
        }
    }

    void accelerate(int increment)
    {
        if (engineRunning)
        {
            speed += increment;
            std::cout << "Accelerating! New speed: " << speed << " km/h\n";
        }
        else
        {
            std::cout << "Engines off  cant accelerate without the engine running, okay?\n";
        }
    }

    void stopEngine()
    {
        if (engineRunning)
        {
            engineRunning = false;
            std::cout << "Engine stopped! Time to relax.\n";
        }
        else
        {
            std::cout << "The engines already off. No problem, folks.\n";
        }
    }

    void displayStatus() const
    {
        std::cout << "Car Status -> Brand: " << this->brand
                  << ", Speed: " << this->speed
                  << " km/h, Engine Running: " << (this->engineRunning ? "Yes" : "No") << "\n";
    }
};

int main()
{
    Car myCar("Ferrari", 100);
    myCar.startEngine();
    myCar.accelerate(50);
    myCar.displayStatus();
    myCar.stopEngine();
    myCar.displayStatus();
    return 0;
}
