import { View, Text, StyleSheet, TextInput, TouchableOpacity, ScrollView } from 'react-native';
import { useState } from 'react';
import { useRouter } from 'expo-router';
import { Lightbulb, Fan, Tv, Lock, Wifi } from 'lucide-react-native';

const deviceTypes = [
  { id: 'light', name: 'Light', icon: Lightbulb },
  { id: 'climate', name: 'Climate', icon: Fan },
  { id: 'entertainment', name: 'Entertainment', icon: Tv },
  { id: 'security', name: 'Security', icon: Lock },
  { id: 'network', name: 'Network', icon: Wifi },
];

export default function AddDeviceScreen() {
  const [deviceName, setDeviceName] = useState('');
  const [selectedType, setSelectedType] = useState(null);
  const [room, setRoom] = useState('');
  const router = useRouter();

  const handleAddDevice = () => {
    // Add device logic here
    router.back();
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.form}>
        <View style={styles.inputGroup}>
          <Text style={styles.label}>Device Name</Text>
          <TextInput
            style={styles.input}
            value={deviceName}
            onChangeText={setDeviceName}
            placeholder="Enter device name"
          />
        </View>

        <View style={styles.inputGroup}>
          <Text style={styles.label}>Device Type</Text>
          <View style={styles.typeGrid}>
            {deviceTypes.map((type) => {
              const Icon = type.icon;
              return (
                <TouchableOpacity
                  key={type.id}
                  style={[
                    styles.typeCard,
                    selectedType === type.id && styles.typeCardSelected,
                  ]}
                  onPress={() => setSelectedType(type.id)}>
                  <Icon
                    size={24}
                    color={selectedType === type.id ? '#ffffff' : '#8E8E93'}
                  />
                  <Text
                    style={[
                      styles.typeText,
                      selectedType === type.id && styles.typeTextSelected,
                    ]}>
                    {type.name}
                  </Text>
                </TouchableOpacity>
              );
            })}
          </View>
        </View>

        <View style={styles.inputGroup}>
          <Text style={styles.label}>Room</Text>
          <TextInput
            style={styles.input}
            value={room}
            onChangeText={setRoom}
            placeholder="Select room"
          />
        </View>

        <TouchableOpacity
          style={[
            styles.addButton,
            (!deviceName || !selectedType || !room) && styles.addButtonDisabled,
          ]}
          onPress={handleAddDevice}
          disabled={!deviceName || !selectedType || !room}>
          <Text style={styles.addButtonText}>Add Device</Text>
        </TouchableOpacity>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F2F2F7',
  },
  form: {
    padding: 20,
  },
  inputGroup: {
    marginBottom: 24,
  },
  label: {
    fontSize: 16,
    fontWeight: '600',
    color: '#000000',
    marginBottom: 8,
  },
  input: {
    backgroundColor: '#ffffff',
    padding: 12,
    borderRadius: 8,
    fontSize: 16,
  },
  typeGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 12,
  },
  typeCard: {
    backgroundColor: '#ffffff',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
    width: '30%',
    aspectRatio: 1,
    justifyContent: 'center',
  },
  typeCardSelected: {
    backgroundColor: '#007AFF',
  },
  typeText: {
    fontSize: 12,
    color: '#8E8E93',
    marginTop: 8,
    textAlign: 'center',
  },
  typeTextSelected: {
    color: '#ffffff',
  },
  addButton: {
    backgroundColor: '#007AFF',
    padding: 16,
    borderRadius: 12,
    alignItems: 'center',
    marginTop: 24,
  },
  addButtonDisabled: {
    backgroundColor: '#8E8E93',
  },
  addButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: '600',
  },
});