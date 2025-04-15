import { Stack } from 'expo-router';

export default function DevicesLayout() {
  return (
    <Stack screenOptions={{ headerShown: false }}>
      <Stack.Screen name="index" />
      <Stack.Screen 
        name="details" 
        options={{
          presentation: 'modal',
          headerShown: true,
          headerTitle: 'Device Details',
        }} 
      />
      <Stack.Screen 
        name="add" 
        options={{
          presentation: 'modal',
          headerShown: true,
          headerTitle: 'Add New Device',
        }} 
      />
    </Stack>
  );
}