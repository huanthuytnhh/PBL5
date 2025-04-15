import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { useLocalSearchParams } from 'expo-router';
import { Power, Settings, History, Signal, Battery } from 'lucide-react-native';

export default function DeviceDetailsScreen() {
  const { id } = useLocalSearchParams();
  
  // In a real app, fetch device details using the ID
  const deviceDetails = {
    name: 'Living Room Light',
    type: 'Light',
    status: 'Connected',
    battery: '85%',
    signal: 'Excellent',
    lastMaintenance: '2024-01-15',
    firmware: 'v2.1.0',
    usage: [
      { time: '2024-02-10 14:30', action: 'Turned On' },
      { time: '2024-02-10 08:15', action: 'Turned Off' },
      { time: '2024-02-09 22:45', action: 'Brightness 70%' },
    ],
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <View style={styles.deviceInfo}>
          <Text style={styles.deviceName}>{deviceDetails.name}</Text>
          <Text style={styles.deviceType}>{deviceDetails.type}</Text>
        </View>
        <TouchableOpacity style={styles.powerButton}>
          <Power size={24} color="#ffffff" />
        </TouchableOpacity>
      </View>

      <View style={styles.statsContainer}>
        <View style={styles.statCard}>
          <Battery size={24} color="#007AFF" />
          <Text style={styles.statValue}>{deviceDetails.battery}</Text>
          <Text style={styles.statLabel}>Battery</Text>
        </View>
        <View style={styles.statCard}>
          <Signal size={24} color="#32ADE6" />
          <Text style={styles.statValue}>{deviceDetails.signal}</Text>
          <Text style={styles.statLabel}>Signal</Text>
        </View>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Device Information</Text>
        <View style={styles.infoCard}>
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Status</Text>
            <Text style={styles.infoValue}>{deviceDetails.status}</Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Last Maintenance</Text>
            <Text style={styles.infoValue}>{deviceDetails.lastMaintenance}</Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={styles.infoLabel}>Firmware Version</Text>
            <Text style={styles.infoValue}>{deviceDetails.firmware}</Text>
          </View>
        </View>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Recent Activity</Text>
        <View style={styles.activityCard}>
          {deviceDetails.usage.map((activity, index) => (
            <View key={index} style={styles.activityRow}>
              <History size={16} color="#8E8E93" />
              <View style={styles.activityInfo}>
                <Text style={styles.activityAction}>{activity.action}</Text>
                <Text style={styles.activityTime}>{activity.time}</Text>
              </View>
            </View>
          ))}
        </View>
      </View>

      <TouchableOpacity style={styles.settingsButton}>
        <Settings size={20} color="#ffffff" />
        <Text style={styles.settingsText}>Device Settings</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F2F2F7',
  },
  header: {
    padding: 20,
    backgroundColor: '#ffffff',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  deviceInfo: {
    flex: 1,
  },
  deviceName: {
    fontSize: 24,
    fontWeight: '700',
    color: '#000000',
  },
  deviceType: {
    fontSize: 16,
    color: '#8E8E93',
    marginTop: 4,
  },
  powerButton: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#007AFF',
    justifyContent: 'center',
    alignItems: 'center',
  },
  statsContainer: {
    flexDirection: 'row',
    padding: 20,
    justifyContent: 'space-between',
  },
  statCard: {
    backgroundColor: '#ffffff',
    padding: 16,
    borderRadius: 12,
    alignItems: 'center',
    width: '48%',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  statValue: {
    fontSize: 20,
    fontWeight: '600',
    marginTop: 8,
    color: '#000000',
  },
  statLabel: {
    fontSize: 14,
    color: '#8E8E93',
    marginTop: 4,
  },
  section: {
    padding: 20,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '600',
    marginBottom: 12,
    color: '#000000',
  },
  infoCard: {
    backgroundColor: '#ffffff',
    borderRadius: 12,
    padding: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#F2F2F7',
  },
  infoLabel: {
    fontSize: 14,
    color: '#8E8E93',
  },
  infoValue: {
    fontSize: 14,
    color: '#000000',
    fontWeight: '500',
  },
  activityCard: {
    backgroundColor: '#ffffff',
    borderRadius: 12,
    padding: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  activityRow: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#F2F2F7',
  },
  activityInfo: {
    marginLeft: 12,
    flex: 1,
  },
  activityAction: {
    fontSize: 14,
    color: '#000000',
  },
  activityTime: {
    fontSize: 12,
    color: '#8E8E93',
    marginTop: 2,
  },
  settingsButton: {
    margin: 20,
    backgroundColor: '#007AFF',
    padding: 16,
    borderRadius: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
  },
  settingsText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: '600',
  },
});